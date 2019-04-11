import setting 
import os
import random
import datetime
from BlueprintArchitech.Library.v1 import performance_intelligent,performance_consistent,performance_intuition,performance_engineering,performance_respondtime

class performance_chart:
	"""docstring"""
	def __init__(self, userid):
		self.userid = userid
		# return
		self.performance_data = {
			'performance_intelligent' 			: performance_intelligent(self.userid),
			'performance_consistent' 			: performance_consistent(self.userid),
			'performance_intuition' 			: performance_intuition(self.userid),
			'performance_engineering' 			: performance_engineering(self.userid),
			'performance_respondtime' 			: performance_respondtime(self.userid),
		}
		# construct chart here