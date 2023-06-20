from ScriptBase import ScriptBase


class ClericScript(ScriptBase):
    def register(self, entityWithProperties):
        super(ClericScript, self).register(entityWithProperties)
        print('    Cleric registered')

    def update(self, entityWithProperties):
        super(ClericScript, self).update(entityWithProperties)
        print('    Cleric updated')