from ScriptBase import ScriptBase


class SkillsScript(ScriptBase):
    def register(self, entityWithProperties):
        super(SkillsScript, self).register(entityWithProperties)
        print('I am registered')
        # raise Exception('Oh Oh')
        pass
    def update(self, entityWithProperties):
        super(SkillsScript, self).update(entityWithProperties)
        print('I am updated')
        pass
