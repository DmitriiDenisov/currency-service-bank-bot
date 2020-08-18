import requests
from flask import Flask, request, jsonify
from wtforms import PasswordField, validators, Form, StringField, DateField, IntegerField, FloatField

from constants import URL, querystring_base, ERROR_CURR
from collections import namedtuple

RespCurr = namedtuple('RespCurr', ['success', 'timestamp', 'base', 'date', 'rates'])


class RatesSchema(Form):
    # filters - function that is applied before validators are checked
    # here upper() is added to make validators case non sensitive
    curr_from = StringField('curr_from', filters=[lambda x: x.upper()],
                            validators=[validators.DataRequired(), validators.AnyOf(['USD', 'EUR', 'AED'])])
    curr_to = StringField('curr_to', filters=[lambda x: x.upper()],
                          validators=[validators.DataRequired(), validators.AnyOf(['USD', 'EUR', 'AED'])])


app = Flask(__name__)


@app.route('/get_rates', methods=['GET'])
def get_rates():
    params = RatesSchema(request.args)
    if not params.validate():
        if ERROR_CURR in params.errors:
            return jsonify({'resp': 'Necessary parameters are not provided!'})
        return jsonify({'resp': 'Currency should be in AED, EUR or USD'})
    querystring = querystring_base.copy()
    from_ = params.curr_from.data
    to_ = params.curr_to.data
    querystring['symbols'] = f'{from_},{to_}'
    response = requests.request("GET", URL, params=querystring)

    if response.status_code == 404:
        return jsonify({'resp': 'API failed!'})
    resp = response.json()
    if not resp:
        return jsonify({'resp': 'API failed!'})
    resp = RespCurr(**resp)
    rate = resp.rates[from_] / resp.rates[to_]

    return jsonify({'rate': rate})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
