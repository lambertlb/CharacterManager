from ScriptBase import ScriptBase


class LongSwordScript(ScriptBase):
    def register(self, entityWithProperties):
        super(LongSwordScript, self).register(entityWithProperties)
        print('Long Sword registered')

    def update(self, entityWithProperties):
        super(LongSwordScript, self).update(entityWithProperties)
        print('Long Sword updated')
