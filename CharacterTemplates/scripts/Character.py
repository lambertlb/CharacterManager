from Entity import Entity


class CharacterScript(Entity):
    def register(self):
        super(CharacterScript, self).register()
        print('Character registered')
        pass
    def update(self):
        super(CharacterScript, self).update()
        print('Character updated')
        pass
