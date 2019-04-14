from flask import Blueprint, render_template, abort, jsonify, request
from BlueprintArchitech.BijakSana.codeathonai.v1 import learn, predict, learn_and_predict
import numpy as np
import json

blueprint = Blueprint('bijaksana', __name__,
                      template_folder='BlueprintArchitech/BijakSana')


@blueprint.route('/learn', methods=['GET', 'POST'])
def learn_it():
    if request.method == 'POST':
        respond = {'status': 200, 'msj': 'POST CALLED'}
        data_target = np.array(
            [float(x) for x in request.form['data_target'].split(',')]).reshape(3, 2)
        result = learn(request.form['userid'], data_target)
        return jsonify(result.modelid)
    else:
        respond = {'status': 200, 'msj': 'GET CALLED'}
        return jsonify(respond)


@blueprint.route('/predict', methods=['GET', 'POST'])
def predict_it():
    if request.method == 'POST':
        respond = {'status': 200, 'msj': 'POST CALLED'}
        img = json.loads(request.data)['data_to_predict']
        result = predict(img)
        return jsonify(result.prediction)
    else:
        respond = {'status': 200, 'msj': 'GET CALLED'}
        return jsonify(respond)


@blueprint.route('/learn_and_predict', methods=['GET', 'POST'])
def learn_and_predict_it():
    if request.method == 'POST':
        respond = {'status': 200, 'msj': 'POST CALLED'}
        data_target = np.array(
            [float(x) for x in request.form['data_target'].split(',')]).reshape(3, 2)
        data_to_predict = np.array(
            [float(x) for x in request.form['data_to_predict'].split(',')]).reshape(1, 2)
        result = learn_and_predict(
            request.form['userid'], data_target, data_to_predict)
        return jsonify(result.prediction)
    else:
        respond = {'status': 200, 'msj': 'GET CALLED'}
        return jsonify(respond)
