from types import FunctionType
from unittest import TestCase

class TestCompileFunctions(TestCase):

	def test_Compile(self):
		functionString = 'def runner(): return "Good"'
		code = compile(functionString, "<string>", "exec")
		foo_func = FunctionType(code.co_consts[0], globals(), "runner")	
		rtn = foo_func()	
		assert rtn == 'Good'

	def test_Compile2(self):
		functionString = 'def runner(arg): return arg'
		code = compile(functionString, "<string>", "exec")
		foo_func = FunctionType(code.co_consts[0], globals(), "runner")	
		rtn = foo_func('Good')	
		assert rtn == 'Good'
