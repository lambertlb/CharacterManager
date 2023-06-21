from configurator.Entity import Entity


class LongSwordScript(Entity):
    def register(self):
        super(LongSwordScript, self).register()
        print('Long Sword registered')

    def update(self):
        super(LongSwordScript, self).update()
        print('Long Sword updated')
