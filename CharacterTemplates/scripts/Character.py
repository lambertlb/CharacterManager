from CharacterServices import CharacterServices
from CharacterTemplates.scripts.CharacterEntity import CharacterEntity
from configurator.Entity import Entity


class Character(CharacterEntity):

	def __init__(self):
		super().__init__()
		self._computedAC = 10
		self.Attributes = None
		self._skillProficiency = 2

	@property
	def skillProficiency(self):
		return self._skillProficiency

	def register(self):
		super().register()

	def update(self):
		enhancements = CharacterServices.getEnhancements()
		enhancements.clear()
		ents = Entity._allEntities
		for entity in Entity._allEntities:
			entity.addEnhanceables(enhancements)
		for entity in Entity._allEntities:
			entity.addEnhancements(enhancements)
		for entity in Entity._allEntities:
			entity.applyEnhancements(enhancements)
		for entity in Entity._allEntities:
			entity.computeBasedOnEnhancements(enhancements)
		pass
