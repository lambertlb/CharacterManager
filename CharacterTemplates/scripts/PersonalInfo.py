from ScriptBase import ScriptBase


class PersonalInfo(ScriptBase):
    def register(self, entityWithProperties):
        super(PersonalInfo, self).register(entityWithProperties)
        print('PersonalInfo registered')
        if not hasattr(entityWithProperties, '_deityScript'):
            entityWithProperties._deityScript = entityWithProperties.loadScript('CharacterTemplates.scripts.Deities.' + entityWithProperties.Deity)
        entityWithProperties._deityScript.register(entityWithProperties)
        if not hasattr(entityWithProperties, '_raceScript'):
            entityWithProperties._raceScript = entityWithProperties.loadScript('CharacterTemplates.scripts.Races.' + entityWithProperties.Race)
        entityWithProperties._raceScript.register(entityWithProperties)

    def update(self, entityWithProperties):
        super(PersonalInfo, self).register(entityWithProperties)
        print('PersonalInfo updated')
        if not hasattr(entityWithProperties, '_raceScript'):
            entityWithProperties._raceScript.update(entityWithProperties)
