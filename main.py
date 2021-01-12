import os

from flask import Flask

from crypto_secret_manager import GCP

app = Flask(__name__)


@app.route('/')
def main() -> str:
    gcp = GCP('91894046703')
    return gcp.get_secret('test-secret', 'latest')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
