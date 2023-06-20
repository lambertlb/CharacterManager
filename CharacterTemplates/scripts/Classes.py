from ScriptBase import ScriptBase


class ClassesScript(ScriptBase):
	"""
	This class will load in the appropriate script for
	handling the specified class. I assumes the following
	1)  The entity with this script has a property called 'Class'
		that contains the name of the class
	2)  The script resides in ./CharacterTemplates/scripts/ClassScripts folder
	3)  The script as the same name as the class I.E. monk.py
	4)  It will then load the script and add it to the entity as _classScript property
	5)  It will then delegate to the script

	Args:
		ScriptBase (_type_): All scripts must subclass ScriptBase
	"""
	def register(self, entityWithProperties):
		super(ClassesScript, self).register(entityWithProperties)
		if not hasattr(entityWithProperties, '_classScript'):
			entityWithProperties._classScript = entityWithProperties.loadScript('CharacterTemplates.scripts.ClassScripts.' + entityWithProperties.Class)
		entityWithProperties._classScript.register(entityWithProperties)

	def update(self, entityWithProperties):
		super(ClassesScript, self).update(entityWithProperties)
		if not hasattr(entityWithProperties, '_classScript'):
			entityWithProperties._classScript.update(entityWithProperties)
