from configurator.Entity import Entity

class Long_Sword(Entity):
    def register(self):
        super(Long_Sword, self).register()
        print('Long Sword registered')

    def update(self, entityWithProperties):
        super(Long_Sword, self).update()
        print('Long Sword updated')

class Unarmed(Entity):
    def register(self):
        super(Unarmed, self).register()
        print('Unarmed registered')

    def update(self, entityWithProperties):
        super(Unarmed, self).update()
        print('Unarmed updated')

class Long_Bow(Entity):
    def register(self):
        super(Long_Bow, self).register()
        print('Long Bow registered')

    def update(self, entityWithProperties):
        super(Long_Bow, self).update()
        print('Long Bow updated')
