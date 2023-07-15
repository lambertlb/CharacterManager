from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from configurator.Entity import Entity


class Offense(CharacterEntity):
	"""
	This class will load in the appropriate script for
	handling the specified weapon. It assumes the following
	1)  The entity with this script has a property called 'Weapon'
		that contains the name of the class
	2)  The script resides in ./CharacterTemplates/scripts/Weapons folder
	3)  The script as the same name as the class I.E. Long_Sword.py
	4)  It will then load the script and add it to the entity as _weaponScript property
	5)  It will then delegate to the script

	"""
	def __init__(self):
		super().__init__()
		self._weaponInfo = None
		self.Weapon = None

	def register(self):
		super().register()
		self._weaponInfo = Entity.instanceFromScript('CharacterTemplates.scripts.Weapons.Weapons#' + self.Weapon)
		self._weaponInfo.register()

	def update(self):
		super().update()
		if self._weaponInfo:
			self._weaponInfo.update()
