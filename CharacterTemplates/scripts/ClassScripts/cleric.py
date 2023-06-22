from CharacterTemplates.scripts.CharacterItem import ClassItem
from configurator.Entity import Entity


class ClericScript(Entity, ClassItem):
	def __init__(self):
		super().__init__()
		self._HitDie = '1d8'

	def register(self):
		super(ClericScript, self).register()
		print('    Cleric registered')

	def update(self):
		super(ClericScript, self).update()
		print('    Cleric updated')
