from ScriptBase import ScriptBase


class TowerShieldScript(ScriptBase):
    def register(self, entityWithProperties):
        super(TowerShieldScript, self).register(entityWithProperties)
        print('Tower Shield registered')

    def update(self, entityWithProperties):
        super(TowerShieldScript, self).update(entityWithProperties)
        print('Tower Shield updated')
