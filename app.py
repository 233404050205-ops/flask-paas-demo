import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    version = os.getenv('APP_VERSION', 'v1')
    message = os.getenv('APP_MESSAGE', 'Welcome to PaaS!')
    return f"<h1>Flask PaaS Demo - {version}</h1><p>{message}</p>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
