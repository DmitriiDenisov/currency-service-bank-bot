import requests
from flask import Flask, request, jsonify

from constants import URL, querystring_base

app = Flask(__name__)


@app.route('/get_rates', methods=['GET'])
def get_rates():
    params = request.args
    querystring = querystring_base.copy()
    from_ = params["from"]
    to_ = params["to"]
    querystring['symbols'] = f'{from_},{to_}'
    response = requests.request("GET", URL, params=querystring)

    if response.status_code == 404:
        return jsonify({'resp': 'API failed!'})
    resp = response.json()
    rate = resp['rates'][to_.upper()] / resp['rates'][from_.upper()]

    return jsonify({'rate': rate})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
