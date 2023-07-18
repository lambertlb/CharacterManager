from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from CharacterTemplates.scripts.Enhancements import Enhancements


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

	def register(self):
		super().register()

	def addEnhancements(self, enhancements: Enhancements):
		if not hasattr(self, 'ClassAddition'):
			return
		for addition in self.ClassAddition:
			for enhance in addition.Enhancements:
				enhancements.addEnhancement(self, enhance.Enhancement, addition.Class, enhance.Amount)
	


