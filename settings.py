from environs import Env

env = Env()
env.read_env('.env')  # read .env file, if it exists

# required variables
TOKEN = env("TOKEN")  # => 'sloria'
# secret = env("SECRET")  # => raises error if not set

# casting
PORT = env.int("PORT")  # => 100

URL = 'http://data.fixer.io/api/latest'
ERROR_CURR = 'Invalid value, must be one of: USD, EUR, AED.'

querystring_base = {
    'access_key': TOKEN,
    'format': '1'
}

# providing a default value
# enable_login = env.bool("ENABLE_LOGIN", False)  # => True
