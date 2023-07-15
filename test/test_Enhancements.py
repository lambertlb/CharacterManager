from unittest import TestCase

from CharacterTemplates.scripts.Enhancements import Enhancements

from configurator.Entity import Entity


class TestEnhancements(TestCase):

	def test_CreateEnhancement(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		assert enhanceable
		assert enhanceable.entity == entity
		assert enhanceable.name == 'ArmorClass'
		assert enhanceable.type == 'integer'
		pass
