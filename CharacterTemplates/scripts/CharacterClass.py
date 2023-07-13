from configurator.Entity import Entity


class CharacterClass(Entity):
	"""
	"""
	def __init__(self):
		super().__init__()
		self.Class = None
		self._classScript = None

	def register(self):
		super().register()
		if not self._classScript:
			self._classScript = Entity.instanceFromScript('CharacterTemplates.scripts.Classes.' + self.Class)
		self._classScript.register()

	def update(self):
		super().update()
		if self._classScript:
			self._classScript.update()
