people = [
  {'name': 'Jack', 'age': 29, 'hobbies': ['games', 'eating']},
  {'name': 'frank', 'age': 30, 'hobbies': ['sports', 'driving']},
  {'name': 'Jeff', 'age': 40, 'hobbies': ['sports', 'running']}
]

people_names = [person['name'] for person in people]
print(people)
print(people_names)

older = all([person ['age'] > 20 for person in people])
print(older)

fixed_people = [person.copy() for person in people]
fixed_people[0]['name'] = 'George'
print(fixed_people)
print(people)

p1, p2, p3 = people
print(p1)
print(p2)
print(p3)