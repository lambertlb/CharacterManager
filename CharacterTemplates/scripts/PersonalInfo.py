from configurator.Entity import Entity


class PersonalInfo(Entity):
	def __init__(self):
		super().__init__()
		self.Deity = None
		self.Race = None
		self._deityScript = None
		self._raceScript = None

	def register(self):
		super(PersonalInfo, self).register()
		print('PersonalInfo registered')
		if not self._deityScript:
			self._deityScript = Entity.instanceFromScript('CharacterTemplates.scripts.Deities.' + self.Deity)
		self._deityScript.register()
		if not self._raceScript:
			self._raceScript = Entity.instanceFromScript('CharacterTemplates.scripts.Races.' + self.Race)
		self._raceScript.register()

	def update(self):
		super(PersonalInfo, self).register()
		print('PersonalInfo updated')
		if self._raceScript:
			self._raceScript.update()
		if self._deityScript:
			self._deityScript.update()
