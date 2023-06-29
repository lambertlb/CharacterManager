from CharacterTemplates.scripts.Armor import Armor
from CharacterTemplates.scripts.Weapons import Weapon
from configurator.Entity import Entity


class CharacterScript(Entity):
	weapons = {}
	armor = {}

	def __init__(self):
		super().__init__()

	def register(self):
		super(CharacterScript, self).register()
		self.filterLists()

	def update(self):
		super(CharacterScript, self).update()
		print('Character updated')

	def filterLists(self):
		entities = Entity.getEntities()
		for entity in entities:
			if isinstance(entity, Weapon):
				CharacterScript.weapons[entity._uuid] = entity
			elif isinstance(entity, Armor):
				CharacterScript.armor[entity._uuid] = entity

		pass