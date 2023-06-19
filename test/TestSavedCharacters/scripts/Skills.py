from ScriptBase import ScriptBase


class TestSkillsScript(ScriptBase):
    def register(self, entityWithProperties):
        super(TestSkillsScript, self).register(entityWithProperties)
        entityWithProperties.registered = True
        pass
    def update(self, entityWithProperties):
        super(TestSkillsScript, self).update(entityWithProperties)
        entityWithProperties.updated = True
        pass
