from CharacterTemplates.scripts.CharacterEntity import CharacterEntity


class ClassInformation(CharacterEntity):
	"""
	This class will load in the appropriate script for
	handling the specified class. It assumes the following
	1)  The entity with this script has a property called 'Class'
		that contains the name of the class
	2)  The script resides in ./CharacterTemplates/scripts/ClassScripts folder
	3)  The script as the same name as the class I.E. monk.py
	4)  It will then load the script and add it to the entity as _classScript property
	5)  It will then delegate to the script
	"""
	def __init__(self):
		super().__init__()
		self._classScript = None

	def register(self):
		super().register()
		# if not self._classScript:
		# 	self._classScript = Entity.instanceFromScript('CharacterTemplates.scripts.ClassScripts.' + self.Class)
		# self._classScript.register()

	def update(self):
		super().update()
		# if self._classScript:
		# 	self._classScript.update()
