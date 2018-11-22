# -*- coding: utf-8 -*-
# another: Jeff.Chen
# ORM框架：peewee的测试用例 
from peewee import *
from datetime import date


db = SqliteDatabase('people.db')


# 定义模型
class Person(Model):
    """
    模型定义：Person
        :param Model: 
    """
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db  # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


db.connect()

db.create_tables([Person, Pet])


# # 插入数据
# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
# uncle_bob.save()  # bob is now stored in the database
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5))

# grandma.name = 'Grandma L.'
# grandma.save()  # Update grandma's name in the database.

# bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
# herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
# herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
# herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

# herb_mittens.delete_instance()

# herb_fido.owner = uncle_bob
# herb_fido.save()

# 查询数据
# grandma = Person.select().where(Person.name == 'Grandma L.').get()
grandma = Person.get(Person.name == 'Grandma L.')
print(grandma.name)

for person in Person.select():
    print(person.name)

# query = Pet.select().where(Pet.animal_type == 'cat')
query = (Pet.select(Pet, Person)
            .join(Person)
            .where(Pet.animal_type == 'cat'))
for pet in query:
    print(pet.name, pet.owner.name)

for pet in Pet.select().join(Person).where(Person.name == 'Bob').order_by(Pet.name):
    print(pet.name)

for person in Person.select().order_by(Person.birthday.desc()):
    print(person.name, person.birthday)

d1940 = date(1940, 1, 1)
d1960 = date(1960, 1, 1)
query = (Person.select().where((Person.birthday.between(d1940, d1960))))

for person in query:
    print(person.name, person.birthday)

for person in Person.select():
    print(person.name, person.pets.count(), 'pets')

query = (Person
         .select(Person, Pet)
         .join(Pet, JOIN.LEFT_OUTER)
         .order_by(Person.name, Pet.name))
for person in query:
    # We need to check if they have a pet instance attached, since not all
    # people have pets.
    if hasattr(person, 'pet'):
        print(person.name, person.pet.name)
    else:
        print(person.name, 'no pets')

db.close()