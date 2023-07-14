import unittest
from unittest import TestCase

import pytest
from CharacterTemplates.scripts.Enhancements import EnhancementCategory, Enhancements

from configurator.Entity import Entity
from configurator.JsonUtils import JsonUtils


class TestEnhancements(TestCase):

	def test_CreateEnhancement(self):
		enhancements = Enhancements()
		entity = Entity()
		enhancement = enhancements.createEnhancement(entity, EnhancementCategory.Abilities, "Strength", 2)
		assert enhancement
		assert enhancement.entity == entity
		assert enhancement.category == EnhancementCategory.Abilities
		assert enhancement.whichToEnhance == 'Strength'
		assert enhancement.howMuch == 2

		assert len(enhancements.allEnhancements) == 1
		assert enhancements.allEnhancements[0] == enhancement
		assert len(enhancements.enhancementsByCategory) == 1
		assert enhancements.enhancementsByCategory[EnhancementCategory.Abilities][0] == enhancement
		pass
