from Entity import Entity


class TestSkillsScript(Entity):
    def register(self):
        super(TestSkillsScript, self).register()
        self.registered = True

    def update(self):
        super(TestSkillsScript, self).update()
        self.updated = True
