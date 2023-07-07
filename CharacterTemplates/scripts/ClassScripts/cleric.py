from CharacterTemplates.scripts.CharacterItem import ClassItem
from configurator.Entity import Entity


class ClericScript(Entity, ClassItem):
	def __init__(self):
		Entity.__init__(self)
		ClassItem.__init__(self)
		self._HitDie = '1d8'
		self._name = 'Cleric'


	def register(self):
		super(ClericScript, self).register()

	def update(self):
		super(ClericScript, self).update()
