from flask import Blueprint, render_template, abort, jsonify, request

blueprint = Blueprint('test_blueprint', __name__,template_folder='BlueprintArchitech/TestScene')
@blueprint.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		respond = {'status' : 200,'msj' : 'POST CALLED'}
		return jsonify(respond)
	else:
		respond = {'status' : 200,'msj' : 'GET CALLED'}
		return jsonify(respond)