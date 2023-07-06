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
		if not self._deityScript and self.Deity != '':
			self._deityScript = Entity.instanceFromScript('CharacterTemplates.scripts.Deities.' + self.Deity)
		if self.Deity != '':
			self._deityScript.register()
		if not self._raceScript and self.Race != '':
			self._raceScript = Entity.instanceFromScript('CharacterTemplates.scripts.Races.' + self.Race)
		if self.Race != '':
			self._raceScript.register()

	def update(self):
		super(PersonalInfo, self).register()
		if self._raceScript:
			self._raceScript.update()
		if self._deityScript:
			self._deityScript.update()

	def getPropertyType(self, propertyName):
		if propertyName == 'Deity':
			return 'composite'
		if propertyName == 'Race':
			return 'composite'
		property = self.definition.get('properties').get(propertyName)
		return property.get('type')
