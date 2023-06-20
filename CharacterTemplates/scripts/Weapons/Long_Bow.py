from ScriptBase import ScriptBase


class LongBowScript(ScriptBase):
    def register(self, entityWithProperties):
        super(LongBowScript, self).register(entityWithProperties)
        print('Long Bow registered')

    def update(self, entityWithProperties):
        super(LongBowScript, self).update(entityWithProperties)
        print('Long Bow updated')
