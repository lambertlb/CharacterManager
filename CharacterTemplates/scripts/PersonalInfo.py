from configurator.Entity import Entity


class PersonalInfo(Entity):
	def __init__(self):
		super().__init__()

	def register(self):
		super(PersonalInfo, self).register()
		print('PersonalInfo registered')
		if not hasattr(self, '_deityScript'):
			self._deityScript = Entity.instanceFromScript('CharacterTemplates.scripts.Deities.' + self.Deity)
		self._deityScript.register()
		if not hasattr(self, '_raceScript'):
			self._raceScript = Entity.instanceFromScript('CharacterTemplates.scripts.Races.' + self.Race)
		self._raceScript.register()

	def update(self):
		super(PersonalInfo, self).register()
		print('PersonalInfo updated')
		if not hasattr(self, '_raceScript'):
			self._raceScript.update()
