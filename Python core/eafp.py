# Duck Typing and Easier to ask forgiveness than permission (EAFP)


# class Duck:

#     def quack(self):
#         print('Quack, quack')

#     def fly(self):
#         print('Flap, Flap!')


# class Person:

#     def quack(self):
#         print("I'm Quacking Like a Duck!")

#     def fly(self):
#         print("I'm Flapping my Arms!")


# def quack_and_fly(thing):
#     pass
# Not Duck-Typed (Non-Pythonic)
# if isinstance(thing, Duck):
# thing.quack()
# thing.fly()
# else:
#     print('This has to be a Duck!')

# LBYL (Non-Pythonic)
# if hasattr(thing, 'quack'):
#     if callable(thing.quack):
#         thing.quack()

# if hasattr(thing, 'fly'):
#     if callable(thing.fly):
#         thing.fly()

#     try:
#         thing.quack()
#         thing.fly()
#         thing.bark()
#     except AttributeError as e:
#         print(e)

#     print()


# d = Duck()
# quack_and_fly(d)
# p = Person()
# quack_and_fly(p)
# print(type(dir(d)))


person = {'name': 'Raj', 'age': 26, 'job': 'Programmer'}
# person = {'name': 'Raj', 'age': 26}

#LBYL (Non-pythonic)
# if 'name' in person and 'age' in person and 'job' in person:
#     print("I'm {name}. I'm {age} years old and I'm a {job}".format(**person))
# else:
#     print('Missing some keys')
# EAFP
try:
    print("I'm {name}. I'm {age} years old and I'm a {job}".format(**person))
except KeyError as e:
    print('Missing {} key'.format(e))
