from configurator.Entity import Entity


class SkillsScript(Entity):
	def __init__(self):
		super().__init__()

	def register(self):
		super(SkillsScript, self).register()
		print('Skills registered')
		pass

	def update(self):
		super(SkillsScript, self).update()
		print('Skills updated')
		pass
