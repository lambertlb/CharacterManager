# need pip install jsonschema

from jsonschema import Draft7Validator, validate

from configurator.JsonUtils import JsonUtils

schemaData = JsonUtils.loadJsonSchema('./CharacterTemplates/CharacterTemplate.json')
Draft7Validator.check_schema(schemaData)
data = JsonUtils.loadJsonFile('./SavedCharacters/Fred.json')
validate(data, schemaData)
