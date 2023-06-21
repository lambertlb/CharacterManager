from configurator.Entity import Entity


class OffenseScript(Entity):
	"""
	This class will load in the appropriate script for
	handling the specified weapon. I assumes the following
	1)  The entity with this script has a property called 'Weapon'
		that contains the name of the class
	2)  The script resides in ./CharacterTemplates/scripts/Weapons folder
	3)  The script as the same name as the class I.E. Long_Sword.py
	4)  It will then load the script and add it to the entity as _weaponScript property
	5)  It will then delegate to the script

	Args:
		ScriptBase (_type_): All scripts must subclass ScriptBase
	"""
	def register(self):
		super(OffenseScript, self).register()
		print('Offense Registered')
		if not hasattr(self, '_weaponScript'):
			self._weaponScript = Entity.instanceFromScript('CharacterTemplates.scripts.Weapons.' + self.Weapon)
		self._weaponScript.register()

	def update(self):
		super(OffenseScript, self).update()
		print('Offense Updated')
		if not hasattr(self, '_weaponScript'):
			self._weaponScript.update()
