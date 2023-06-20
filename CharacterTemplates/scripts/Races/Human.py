from ScriptBase import ScriptBase


class HumanScript(ScriptBase):
    def register(self, entityWithProperties):
        super(HumanScript, self).register(entityWithProperties)
        print('Human registered')

    def update(self, entityWithProperties):
        super(HumanScript, self).update(entityWithProperties)
        print('Human updated')
