from configurator.Logger import Logger


class TestLogger(Logger):
	def __init__(self):
		self._lastLogged = None

	@property
	def lastLogged(self):
		return self._lastLogged
	
	def clear(self):
		self._lastLogged = None

	def log(self, whatToLog):
		self._lastLogged = whatToLog
		print(whatToLog)

	def logException(self, whatToLog, exception: Exception):
		self._lastLogged = whatToLog
		pass