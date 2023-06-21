from Entity import Entity


class SuneScript(Entity):
    def register(self):
        super(SuneScript, self).register()
        print('Sune registered')

    def update(self):
        super(SuneScript, self).update()
        print('Sune updated')
