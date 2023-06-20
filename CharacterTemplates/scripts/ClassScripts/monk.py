from ScriptBase import ScriptBase


class MonkScript(ScriptBase):
    def register(self, entityWithProperties):
        super(MonkScript, self).register(entityWithProperties)
        print('    Monk registered')
        pass
    def update(self, entityWithProperties):
        super(MonkScript, self).update(entityWithProperties)
        print('    Monk updated')
        pass
