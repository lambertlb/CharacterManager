from Logger import Logger


class TestLogger(Logger):
	def __init__(self):
		self._lastLogged = None

	@property
	def lastLogged(self):
		return self._lastLogged

	def log(self, whatToLog):
		self._lastLogged = whatToLog

	def logException(self, whatToLog, exception: Exception):
		self._lastLogged = whatToLog
		pass