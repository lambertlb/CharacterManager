from ScriptBase import ScriptBase


class PlateMailScript(ScriptBase):
    def register(self, entityWithProperties):
        super(PlateMailScript, self).register(entityWithProperties)
        print('Plate Mail registered')

    def update(self, entityWithProperties):
        super(PlateMailScript, self).update(entityWithProperties)
        print('Plate Mail updated')
