from configurator.Entity import Entity


class SkillsScript(Entity):
    def register(self):
        super(SkillsScript, self).register()
        print('Skills registered')
        pass

    def update(self):
        super(SkillsScript, self).update()
        print('Skills updated')
        pass
