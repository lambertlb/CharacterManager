from CharacterTemplates.scripts.Enhancements import Enhancements
from configurator.Entity import Entity


class CharacterEntity(Entity):

	def __init__(self):
		super().__init__()

	def addEnhanceables(self, enhancements: Enhancements):
		pass

	def addEnhancements(self, enhancements: Enhancements):
		pass

	def applyEnhancements(self, enhancements: Enhancements):
		pass

	def computeBasedOnEnhancements(self, enhancements: Enhancements):
		pass
