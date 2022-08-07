
from flask import Flask
from flask_cors import CORS
from controller.hubbridge import hubBridge


app = Flask(__name__)
CORS(app)

app.register_blueprint(hubBridge)

@app.route('/')
def hello_world():
    return 'Não Autorizado'


if __name__ == '__main__':
    app.run()
