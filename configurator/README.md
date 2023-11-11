# Configurator Elements
This document will attempt to explain what the elements of the configurator are and how to use them.

## Configurator Purpose
The purpose of the items in this folder is to create an infrastructure for managing information for configuring most anything. Most systems are made up of elements that contain options. So most systems have a way of exporting and importing data to set up those options. It turns out that functionally they all do basically the same thing. Some use custom files , XML , and json for holding the exported data. Most then have custom code for doing the importing and exporting. As the data gets more complex and new option are required the code ends up getting more complex causing many issues making it difficult to enhance the data. The purpose of the configurator files are to give a simple and extendable way of managing this data.

## Theory behind the configurator and its goals
Following are a few bullet points that hopefully help explain the theory behind what is trying to be accomplished.
- Data is made up of Objects that contain properties.

  These objects should be able to describe all information needed by the system
- Properties of an object can contain the following information.

  1) Strings - Textual data
  2) Integers - 64 bit integer data
  3) Numbers - Floating point numbers
  4) Booleans - True or false values
  5) Objects - Other objects that contain properties
  6) Arrays - A list of previously mention types.

- Objects should be able to be validated.

  This means there needs to be a separate set of schema files with information that can be used to validate the structure of the data.
- Data and Schema should be extensible without major rework of existing items.

  There should be a way of enhancing existing data without major reworks. This is to cut down on the effort needed to validate existing data and code.
- Schema should be able to specify the code that manages a specific set of data.
  
  This is so custom code can be added for managing data without having to change existing code. This is to cut down on maintenance issues. Only the new code needs to be validated.

## Json
The files in this folder will manage data in such a way as to accomplish the goals set out in the theory. Json will be used to do that. It was chosen because it is human readable, compact, and can be validated with a schema also written in Json. The schema specification also has elements in it to allow for enhancements. For example $ref can be use to reference another file. So new data and its schema can be added to separate files and by using $ref it can be included by only adding a single $ref to the original file. Another benefit is that Json is natively supported by most modern languages. The schema also allows for custom definitions. For example data may need to have modifiers to help describe itself. By adding a new term like $modifiers this can be easily accomplished

## Files in Configurator
- Services.py

  This is a small utility class used to help decouple components. This is so components like a configuration manager or logger can be swapped out by others to help doing things like unit testing. I found this better than dependency injection because many projects can contain tons of tiny worker classes and it becomes a mess to do injections everywhere. A single static class just seemed simpler to me. Especially in the context of this package where specific code can be added dynamically to handle custom data making dependency injection more difficult.

- Logger.py

  Base class for creating a system specific logger. Just subclass this and add your own functionality. Make sure to make it available by calling setLogger on Services.

- ConfigurationManager.py

  Base class for managing configurations. The default implementation will manage configuration items in an .ini file. This files will contain sections with specific data in them. You need to subclass this add you system specific config data. Make sure to make it available by calling setConfigurationManager on Services.

- JsonUtils.py

  This file contain functions for handling Json data. For doing things like read or writing json files and read json schema.

- Entity.py

  This is a file that manages Entities. Entities are the objects mentioned in the theory. They are called entities instead of objects to avoid name collision with most computer languages that have the base class for all items as Object.

## Scripts for customizing schema
Scripts can be used to customize data handling. The $script tag is used to do this. This is a custom tag created specifically to allow the adding of custom python scripts to enhance data management. Following are some short examples on how it can be done.

Let's assume we have some json data describing a fantasy warrior character and we want to add support for a handling weapons that didn't exist before. First we add some data into the warriors json data. This data will be an property called Offense that holds an array various weapons
```
{
    "ExistingData": "old data",
	"Offense": {
		"Weapons": [
			{
				"Weapon": "Long Sword",
			},
			{
				"Weapon": "Long Bow"
			},
			{
				"Weapon": "Unarmed"
			}
		]
	}
}
```
Now we need the schema to make this valid and also add custom code to handle the weapons. Following is how that can be done.
```
{
	"$schema": "https://json-schema.org/draft/2020-12/schema",
	"type": "object",
	"properties": {
        "ExistingData": {
            "type": "string"
        },
		"Offense": {
			"type": "object",
			"$script": {
				"className": "CharacterTemplates.scripts.Offense"
			},
			"properties": {
				"Weapons": {
					"type": "array",
					"items": {
						"type": "object",
						"$script": {
							"className": "CharacterTemplates.scripts.OffensiveItem"
						},
						"properties": {
							"Weapon": {
								"type": "string"
							}
						}
					}
				}
			}
		}
    }
}
```
As you can see the "Offense" property has been added declaring an array of objects. Also note the use of the $script tag. This means for every object in this array use the python script to create it. The className property uses python namespace nomenclature. In the example it means look in sub-folders CharacterTemplates then scripts to find file OffensiveItem.py. It will then look in that file for a class that is a subclass of Entity and use that to house the element of the array.

Lets look at part this class.
```
from configurator.Entity import Entity

class OffensiveItem(Entity):
	def __init__(self):
		super().__init__()
		self._weaponInfo = None
		self.Weapon = None

	def register(self):
		super().register()
		self._weaponInfo = Entity.instanceFromScript('CharacterTemplates.scripts.Weapons#' + self.Weapon)
		self._weaponInfo.register()
```
This class is a subclass of Entity. It will end up holding one instance of data from the Offense array. For example the first element will have its self.Weapon property set to "Long Sword". Also note that we also need to manage code specific to that long sword. So in the register method we call Entity.instanceFromScript with the namespace for a class to handle the long sword data. This will look for a Long_Sword class in a file called Weapons.py in path ./CharacterTemplates/scripts.

## Schema Summary
So you can see that by adding a simple custom tag ($script) to a schema I was able to do two levels of customization for handling the data. I.E. handling the offense array elements and custom code for each element in the array.

## Data modifications
Data modification can be added in many ways. I will show one way I did it. Following is a example of how i modified the previous example so the program can tell if a weapon is currently equipped. Following is the data with the modifications
```
{
    "ExistingData": "old data",
	"Offense": {
		"Weapons": [
			{
				"Weapon": "Long Sword",
				"$modifiers": {
					"_isEquipped": true
				}
			},
			{
				"Weapon": "Long Bow"
			},
			{
				"Weapon": "Unarmed"
			}
		]
	}
}
```
Note that i added a custom tag called modifiers. It has a property call isEquipped set to true. Now i need code to handle this. From the previous example we assumed we have a Weapons.py file with a class called Long_Sword to handle that. This class is a subclass of Entity. Let's modify that to facilitate modifications. First we can create a class to define all possible modifications and how to handle them.
```
class CharacterItem:
	def __init__(self):
		self._description = ''
		self._weight = 0
		self._cost = 0
        self._isEquipped = False
    
	def register(self):
		self.handleModifiers(self, self)

	def handleModifiers(self, itemWithModifiers):
		if not hasattr(itemWithModifiers, '$modifiers'):
			return
		modifiers = getattr(itemWithModifiers, '$modifiers')
		for propertyList in list(modifiers.items()):
			propertyName, data = propertyList
			propertyToSet = '_' + propertyName
			if hasattr(self, propertyToSet):
				setattr(self, propertyToSet, data)

```
When this class is registered after an instance is created it will search for the $modifiers tag and go through the list and set the appropriate property on itself. In our case it will take "isEquipped" data and set the property self._isEquipped to true. Now lets look at the Long_Sword class
```
class Weapon(CharacterItem):
	def __init__(self):
		super().__init__()


class Long_Sword(Entity, Weapon):
	def __init__(self):
		Entity.__init__(self)
		Weapon.__init__(self)
		self._description = 'Big Long Sword'
		self._weight = 5
		self._cost = 75
	
	def register(self):
		super().register()
```
First we created a Weapon class to house weapon specific information. All weapons should derive from this. Then we created a Long_Sword class. This class uses multiple inheritance. It must inherit from Entity so it works with the $script tag then it also inherits from Weapon to get all the possible modifiers. Once the instance is created and the register method is called all the modifiers in the $modifiers tag will be applied. In this case self._isEquipped will be set to True

## Conclusion
Hopefully i have shown how I was able to add data and schema with code to support them without any changes at all to the base code. This should allow for complex management of data without the need for a lot of infrastructure support. Both the json data and schema files can be put under source code management to facilitate management of change.
