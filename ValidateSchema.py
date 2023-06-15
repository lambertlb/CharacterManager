# need pip install jsonschema

from jsonschema import Draft7Validator, validate
import json

from JsonUtils import JsonUtils

schemaData = JsonUtils.loadJsonFile('./CharacterTemplates/CharacterTemplate.json')
Draft7Validator.check_schema(schemaData)
data = JsonUtils.loadJsonFile('./SavedCharacters/Fred.json')
validate(data,schemaData)
