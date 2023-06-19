from ScriptBase import ScriptBase


class TestSkillsScript(ScriptBase):
    def register(self, entityWithProperties):
        super(TestSkillsScript, self).register(entityWithProperties)
        assert False

    def update(self, entityWithProperties):
        super(TestSkillsScript, self).update(entityWithProperties)
        entityWithProperties.updated = True
