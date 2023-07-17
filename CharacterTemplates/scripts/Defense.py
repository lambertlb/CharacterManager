from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from configurator.Entity import Entity


class Defense(CharacterEntity):
	"""
	This class will load in the appropriate script for
	handling the specified armor. It assumes the following
	1)  The entity with this script has a property called 'Armor'
		that contains the name of the class
	2)  The script resides in ./CharacterTemplates/scripts/Armor folder
	3)  The script as the same name as the class I.E. PlateMail.py
	4)  It will then load the script and add it to the entity as _armorScript property
	5)  It will then delegate to the script
	"""

	def __init__(self):
		super().__init__()
		self._armorInfo = None
		self.Defense = None

	def register(self):
		super().register()
		self._armorInfo = Entity.instanceFromScript('CharacterTemplates.scripts.Armor.Armor#' + self.Defense)
		self._armorInfo.register()
		self._armorInfo.handleModifiers(self)

	def update(self):
		super().update()
		if self._armorInfo:
			self._armorInfo.update()
