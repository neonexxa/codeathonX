from sklearn import svm #contoh
import setting 
import pickle
import os
import random
import datetime

class learn:
	"""docstring"""
	def __init__(self, userid, data_target):
		X = data_target[:-1]
		Y = data_target[-1]
		self.model_fitted = svm.SVC(gamma=0.001).fit(X, Y) #contoh
		# save model here
		model_key = str(random.randint(100000000000,999999999999))
		today = str(datetime.date.today())
		pickle_meta = { 
			'created_at':today,
			'model_key':model_key }
		model_id = str(hash(frozenset(pickle_meta.items())))
		path = setting.model_folder+"/"+userid+"/"+model_id+".pkl"
		pickle.dump(self.model_fitted, open(path, 'wb'))
		# return
		self.modelid = {
			'result' 			: model_id,#list(self.model_fitted.predict(data_to_predict)),# return kan modelid
		}

class predict:
	"""docstring"""
	def __init__(self, userid, modelid, data_to_predict):
		# load model here
		path = setting.model_folder+"/"+userid+"/"+modelid+".pkl"
		loaded_model = pickle.load(open(path, 'rb'))
		# return
		self.prediction = {
			'result' 			: list(loaded_model.predict(data_to_predict)),
		}

class learn_and_predict:
	"""docstring"""
	def __init__(self, userid, data_target, data_to_predict):
		X = data_target[:-1]
		Y = data_target[-1]
		self.model_fitted = svm.SVC(gamma=0.001).fit(X, Y)

		# return
		self.prediction = {
			'result' 			: list(self.model_fitted.predict(data_to_predict)),
		}