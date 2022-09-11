
from flask import Flask
from flask_cors import CORS

from controller.exception import hubExcept
from controller.hubbridge import hubBridge


app = Flask(__name__)
CORS(app)

app.register_blueprint(hubBridge)
app.register_blueprint(hubExcept)

@app.route('/')
def starter():
    return 'Não Autorizado'

if __name__ == '__main__':
    app.run()
