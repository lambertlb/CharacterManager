from ScriptBase import ScriptBase


class DefenseScript(ScriptBase):
	"""
	This class will load in the appropriate script for
	handling the specified armor. I assumes the following
	1)  The entity with this script has a property called 'Armor'
		that contains the name of the class
	2)  The script resides in ./CharacterTemplates/scripts/Armor folder
	3)  The script as the same name as the class I.E. Platemail.py
	4)  It will then load the script and add it to the entity as _armorScript property
	5)  It will then delegate to the script

	Args:
		ScriptBase (_type_): All scripts must subclass ScriptBase
	"""
	def register(self, entityWithProperties):
		super(DefenseScript, self).register(entityWithProperties)
		print('Defense Registered')
		if not hasattr(entityWithProperties, '_armorScript'):
			entityWithProperties._armorScript = entityWithProperties.loadScript('CharacterTemplates.scripts.Armor.' + entityWithProperties.Defense)
		entityWithProperties._armorScript.register(entityWithProperties)

	def update(self, entityWithProperties):
		super(DefenseScript, self).update(entityWithProperties)
		print('Defense Updated')
		if not hasattr(entityWithProperties, '_armorScript'):
			entityWithProperties._armorScript.update(entityWithProperties)
