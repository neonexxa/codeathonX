from flask import Blueprint, render_template, abort, jsonify, request
from BlueprintArchitech.Dashboard.performance.v1 import performance_chart
import numpy as np
import json
import plotly
import plotly.graph_objs as go

blueprint = Blueprint('dashboard', __name__,template_folder='BlueprintArchitech/Dashboard')
@blueprint.route('/performance', methods=['GET','POST'])
def performance():
	if request.method == 'POST':
		respond = {'status' : 200,'msj' : 'POST CALLED'}
		user_performance = performance_chart(request.form['userid'])
		print(user_performance.performance_data)
		return jsonify(user_performance)
	else:
		respond = {'status' : 200,'msj' : 'GET CALLED'}
		user_performance = performance_chart("1213131312")
		print(user_performance.performance_data)
		uspv = list(user_performance.performance_data.values())
		uspk = []
		for i in list(user_performance.performance_data.keys()):
			print(i.split('_')[1])
			uspk.append(i.split('_')[1])
		return render_template('dashboard/performance.html',pagetitle="Performance",uspv=uspv,uspk=uspk)