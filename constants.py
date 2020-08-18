with open("token.txt") as file:
    TOKEN = file.readline()

URL = 'http://data.fixer.io/api/latest'
ERROR_CURR = 'Invalid value, must be one of: USD, EUR, AED.'

querystring_base = {
    'access_key': TOKEN,
    'format': '1'
}
