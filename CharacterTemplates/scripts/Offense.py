from ScriptBase import ScriptBase


class OffenseScript(ScriptBase):
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
	def register(self, entityWithProperties):
		super(OffenseScript, self).register(entityWithProperties)
		print('Offense Registered')
		if not hasattr(entityWithProperties, '_weaponScript'):
			entityWithProperties._weaponScript = entityWithProperties.loadScript('CharacterTemplates.scripts.Weapons.' + entityWithProperties.Weapon)
		entityWithProperties._weaponScript.register(entityWithProperties)

	def update(self, entityWithProperties):
		super(OffenseScript, self).update(entityWithProperties)
		print('Offense Updated')
		if not hasattr(entityWithProperties, '_weaponScript'):
			entityWithProperties._weaponScript.update(entityWithProperties)
