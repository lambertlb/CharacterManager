from CharacterServices import CharacterServices
from configurator.Entity import Entity


class ClassAdditions(Entity):
	"""
	"""
	def __init__(self):
		super().__init__()
		self._enhancements = []

	def register(self):
		super().register()
		for key in self.data.keys():
			prop = getattr(self, key)
			if prop:
				enhancements = prop.get('Enhancements')
				if enhancements:
					self.handleEnhancements(enhancements)
				spells = prop.get('Spells')
				if spells:
					self.handleSpells(spells)
		enhancementManager = CharacterServices.getEnhancements()
		pass


	def update(self):
		super().update()

	def handleEnhancements(self, enhancements):
		enhancementManager = CharacterServices.getEnhancements()
		for enhancement in enhancements:
			self._enhancements.append(enhancementManager.addEnhancement(enhancement, self))
		pass

	def handleSpells(self, spells):
		pass
