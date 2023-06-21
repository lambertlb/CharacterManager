from configurator.Entity import Entity


class HumanScript(Entity):
    def register(self):
        super(HumanScript, self).register()
        print('Human registered')

    def update(self):
        super(HumanScript, self).update()
        print('Human updated')
