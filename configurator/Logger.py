import traceback


class Logger:

	# noinspection PyMethodMayBeStatic
	def log(self, whatToLog):
		print(whatToLog)

	# noinspection PyMethodMayBeStatic
	def logException(self, whatToLog, exception: Exception):
		print(whatToLog)
		print(exception)
		traceback.print_tb(exception.__traceback__)
