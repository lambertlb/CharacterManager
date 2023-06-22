from CharacterTemplates.scripts.CharacterItem import ClassItem
from configurator.Entity import Entity


class MonkScript(Entity, ClassItem):
	def __init__(self):
		super().__init__()
		self._HitDie = '1d8'

	def register(self):
		super(MonkScript, self).register()
		print('    Monk registered')

	def update(self, entityWithProperties):
		super(MonkScript, self).update()
		print('    Monk updated')
