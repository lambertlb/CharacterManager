from Logger import Logger


class TestLogger(Logger):
	def __init__(self):
		super(TestLogger, self).__init__()
		self._lastLogged = None

	@property
	def lastLogged(self):
		return self._lastLogged

	def Log(self, whatToLog):
		self._lastLogged = whatToLog
