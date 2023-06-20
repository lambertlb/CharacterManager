from ScriptBase import ScriptBase


class SuneScript(ScriptBase):
    def register(self, entityWithProperties):
        super(SuneScript, self).register(entityWithProperties)
        print('Sune registered')

    def update(self, entityWithProperties):
        super(SuneScript, self).update(entityWithProperties)
        print('Sune updated')
