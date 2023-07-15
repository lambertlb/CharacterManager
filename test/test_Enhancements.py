from unittest import TestCase

import pytest

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
		assert len(enhanceable.enhancements) == 0
		assert len(enhancements.enhanceableItems) == 1
		assert enhancements.enhanceableItems.get('ArmorClass')
		assert enhancements.enhanceableItems.get('ArmorClass') == enhanceable

	def test_CreateEnhancement2(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		with pytest.raises(Exception):
			enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		

	def test_FindEnhanceable(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		found = enhancements.findEnhanceable('NothingToFind')
		assert not found
		found = enhancements.findEnhanceable('ArmorClass')
		assert found

	def test_AddEnhancement(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		enhancement = enhancements.addEnhancement(entity, 'ArmorClass', 'Monk Unarmored', 8)
		assert enhancement
		assert enhancement.entity == entity
		assert enhancement.description == 'Monk Unarmored'
		assert enhancement.value == 8

	def test_AddEnhancement2(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		with pytest.raises(Exception):
			enhancement = enhancements.addEnhancement(entity, 'Bad Key', 'Monk Unarmored', 8)

	def test_AddEnhancement3(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		with pytest.raises(Exception):
			enhancement = enhancements.addEnhancement(entity, 'ArmorClass', 'Monk Unarmored', 'bad value')

	def test_GetEnhancements(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		enhancement = enhancements.addEnhancement(entity, 'ArmorClass', 'Monk Unarmored', 8)
		enhancement2 = enhancements.addEnhancement(entity, 'ArmorClass', 'Bracers of armor', 2)
		enhancements = enhancements.getEnhancements('ArmorClass')
		assert enhancements
		assert len(enhancements) == 2
		assert enhancements[0] == enhancement
		assert enhancements[1] == enhancement2

	def test_GetEnhancements2(self):
		enhancements = Enhancements()
		entity = Entity()
		enhanceable = enhancements.addItemThatCanBeEnhanced(entity, 'ArmorClass', 'integer')
		enhancement = enhancements.addEnhancement(entity, 'ArmorClass', 'Monk Unarmored', 8)
		with pytest.raises(Exception):
			enhancements = enhancements.getEnhancements('Test')
