from flask import Flask, request, jsonify
from flask_cors import CORS
from BlueprintArchitech import TestScene, BijakSana, Dashboard
 
app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(TestScene.blueprint,url_prefix='/')
app.register_blueprint(BijakSana.blueprint,url_prefix='/bijaksana')
app.register_blueprint(Dashboard.blueprint,url_prefix='/dashboard')

if __name__ == "__main__":
    app.run(threaded=True,host='0.0.0.0')