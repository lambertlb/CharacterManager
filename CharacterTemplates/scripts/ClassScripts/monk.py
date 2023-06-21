from configurator.Entity import Entity


class MonkScript(Entity):
    def register(self):
        super(MonkScript, self).register()
        print('    Monk registered')
        pass
    def update(self, entityWithProperties):
        super(MonkScript, self).update()
        print('    Monk updated')
        pass
