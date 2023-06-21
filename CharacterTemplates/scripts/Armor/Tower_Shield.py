from configurator.Entity import Entity


class TowerShieldScript(Entity):
    def register(self):
        super(TowerShieldScript, self).register()
        print('Tower Shield registered')

    def update(self):
        super(TowerShieldScript, self).update()
        print('Tower Shield updated')
