from configurator.Entity import Entity


class TestSkillsScript(Entity):
    def register(self):
        super(TestSkillsScript, self).register()
        assert False

    def update(self):
        super(TestSkillsScript, self).update(entityWitProperties)
        self.updated = True
