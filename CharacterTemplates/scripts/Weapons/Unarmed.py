from configurator.Entity import Entity


class UnarmedScript(Entity):
    def register(self):
        super(UnarmedScript, self).register()
        print('Unarmed registered')

    def update(self, entityWithProperties):
        super(UnarmedScript, self).update()
        print('Unarmed updated')
