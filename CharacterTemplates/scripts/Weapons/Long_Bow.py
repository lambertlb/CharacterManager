from configurator.Entity import Entity


class LongBowScript(Entity):
    def register(self):
        super(LongBowScript, self).register()
        print('Long Bow registered')

    def update(self, entityWithProperties):
        super(LongBowScript, self).update()
        print('Long Bow updated')
