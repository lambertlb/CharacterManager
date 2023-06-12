from jsonschema import Draft7Validator, validate
import json

from JsonUtils import JsonUtils

schemaData = JsonUtils.loadJsonFile('./test/TestSavedCharacters/CharacterSchema.json')
Draft7Validator.check_schema(schemaData)
data = JsonUtils.loadJsonFile('./test/TestSavedCharacters/Character_1.json')
validate(data,schemaData)
