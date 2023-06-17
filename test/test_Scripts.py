import importlib
import inspect
import os
import pkgutil
from unittest import TestCase
from urllib.parse import urlsplit


class TestScripts(TestCase):

	def test_FindScripts(self):
		pkg_path = os.path.abspath('.') + '/CharacterTemplates/scripts'
		for _, name, ispkg in pkgutil.iter_modules([pkg_path], 'CharacterTemplates.scripts.'):
			if ispkg:
				continue
			module = importlib.import_module(name)
			members = inspect.getmembers(module)
			for member in members:
				name , item = member
				if inspect.isclass(item):
					if name != 'ScriptBase':
						print(name)
		pass
