with open("token.txt") as file:
    TOKEN = file.readline()

URL = 'http://data.fixer.io/api/latest'

querystring_base = {
    'access_key': TOKEN,
    'format': '1'
}