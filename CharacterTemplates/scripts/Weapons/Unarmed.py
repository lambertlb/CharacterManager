from ScriptBase import ScriptBase


class UnarmedScript(ScriptBase):
    def register(self, entityWithProperties):
        super(UnarmedScript, self).register(entityWithProperties)
        print('Unarmed registered')

    def update(self, entityWithProperties):
        super(UnarmedScript, self).update(entityWithProperties)
        print('Unarmed updated')
