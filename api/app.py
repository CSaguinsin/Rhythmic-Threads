from os import getenv

from apiflask import APIFlask
from dotenv import load_dotenv

app = APIFlask(__name__, title="Rhythmic Threads API", version='0.1.0')
app.info = {
    'description': 'API documentation for interacting with Rhythmic Threads API',
    'contact': {
        'name': 'API Support',
        'url': 'https://m.me/jhdcruz',
        'email': 'jhdcruz@proton.me'
    },
    'license': {
        'name': 'Licensed under Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html'
    }
}


load_dotenv()


@app.route('/')
def hello_world():
    return 'Hello, World!'


debug = getenv('DEBUG', False)
if __name__ == '__main__':
    app.run(debug=debug)
