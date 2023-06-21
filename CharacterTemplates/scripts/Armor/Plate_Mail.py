from Entity import Entity


class PlateMailScript(Entity):
    def register(self):
        super(PlateMailScript, self).register()
        print('Plate Mail registered')

    def update(self):
        super(PlateMailScript, self).update()
        print('Plate Mail updated')
