from ScriptBase import ScriptBase


class ClassesScript(ScriptBase):
    def register(self, entityWithProperties):
        super(ClassesScript, self).register(entityWithProperties)
        if not hasattr(entityWithProperties, '_classScript'):
            entityWithProperties._classScript = entityWithProperties.loadScript('CharacterTemplates.scripts.ClassScripts.' + entityWithProperties.Class)
        entityWithProperties._classScript.register(entityWithProperties)
        pass

    def update(self, entityWithProperties):
        super(ClassesScript, self).update(entityWithProperties)
        if not hasattr(entityWithProperties, '_classScript'):
            entityWithProperties._classScript.update(entityWithProperties)
        pass
