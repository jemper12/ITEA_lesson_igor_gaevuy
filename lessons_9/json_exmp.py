import json


class Person:
    def __init__(self, first_name, surname, age):
        self._first_name = first_name
        self._surname = surname
        self._age = age


class PersonEncoder(json.JSONEncoder):
    def default(self, person_not):
        if isinstance(person_not, Person):
            return person.__dict__
        else:
            return json.JSONEncoder.default(person_not, Person)


person = {
    'first_name': 'Igor',
    'surname': 'Gaevuy',
    'age': 30,
    'interested': ('footbol', 'music')
}

with open('my.json', 'w') as file:
    json.dump(person, file, indent=4)
print(type(person))
person_serialized = json.dumps(person, indent=4)
print(person_serialized)

person_deserialized = json.loads(person_serialized)
print(type(person_deserialized))

person_obj = Person('igor', 'asdasd', 431)
person_serialized_class = json.dumps(person_obj, cls=PersonEncoder, indent=4)

print(person_serialized_class)
