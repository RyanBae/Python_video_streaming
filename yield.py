import itertools

print("\n====================================")
print(":: Create Generator  \n")
gen = (x*x for x in [1, 2, 3, 4, 5])
array_gen = [x*x for x in [1, 2, 3, 4, 5]]

print(gen)
print(list(gen))
print(array_gen)

gen2 = [1, 2, 3, 4, 5]
gen3 = (x*x for x in [1, 2, 3, 4, 5])
print(gen2)
print(type(gen2))
print(gen3)
print(type(gen3))


print("\n====================================")
print(":: Generator and yield \n")


def one_generator():
    yield 1
    yield 2
    return 'End generator'


try:
    g = one_generator()
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)

print("\n====================================")
print(":: Create generator \n")


def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1

    return "End generator"


print(':For Each > ')
for i in number_generator(3):
    print(i)

print('\n:Variable > ')
g = number_generator(5)
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)

print("\n====================================")
print(":: Calling a function in yield \n")


def upper_generator(x):
    for i in x:
        yield i


fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)

print("\n====================================")
print(":: yield from\n")

print(':gennerate for yield > ')


def number_generator2():
    x = [1, 2, 3]
    for i in x:
        yield i


for i in number_generator2():
    print(i)

print('\n:gennerator yield from iterable > ')


def number_generator3():
    x = [1, 2, 3]
    yield from x
    return 'End generator'


for i in number_generator3():
    print(i)

print(number_generator3())

print('\n:--- ')
g = number_generator3()
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)


print("\n====================================")
print(":: yield from object \n")


def number_generator4(stop):
    n = 0
    while n < stop:
        yield n
        n += 1


def three_generator():
    yield from number_generator4(3)


for i in three_generator():
    print(i)

print('\n:--- ')
g = number_generator4(3)

print('\n: Generator list ')
print('\n: object > ')
print(g)
print('\n: list > ')
print(list(g))

print('\n: ')
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(e)

print("\n====================================")
print("::  Itertools \n")

# import itertools

horses = [1, 2, 3, 4]
races = itertools.permutations(horses)
print(races)
print(list(itertools.permutations(horses)))
