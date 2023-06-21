from configurator.Entity import Entity


class ClericScript(Entity):
    def register(self):
        super(ClericScript, self).register()
        print('    Cleric registered')

    def update(self):
        super(ClericScript, self).update()
        print('    Cleric updated')
