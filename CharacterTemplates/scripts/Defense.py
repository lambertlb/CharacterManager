from configurator.Entity import Entity


class DefenseScript(Entity):
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
	def register(self):
		super(DefenseScript, self).register()
		print('Defense Registered')
		self._armorScript = Entity.instanceFromScript('CharacterTemplates.scripts.Armor#' + self.Defense)
		self._armorScript.register()

	def update(self):
		super(DefenseScript, self).update()
		print('Defense Updated')
		if not hasattr(self, '_armorScript'):
			self._armorScript.update()
