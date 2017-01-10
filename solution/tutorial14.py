#!/usr/bin/env python3


class Person:
    """
    Class representing a person with `name`, `sex` and `age`.
    """

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self):
        return '%s-%d-%s' % (self.name, self.age, self.sex)

    def __repr__(self):
        return str(self)


def find_older_than(people, age):
    """
    Find all people older than (strictly) given `age`.

    :param people: `list` of people as instances of `Person`
    :param age: `age` for `people` filtering
    :return: `list` of all people older than `age`
    """
    result = []
    for p in people:
        if p.age > age:
            result.append(p)
    return result


def find_men(people):
    """
    Find all men.

    :param people: `list` of people as instances of `Person`
    :return: `list` of all people with `sex` equal to `'man'`
    """
    result = []
    for p in people:
        if p.sex == 'man':
            result.append(p)
    return result


def find_men_older_than(people, age):
    """
    Find all men older than (strictly) given `age`.

    :param people: `list` of people as instances of `Person`
    :param age: `age` for `people` filtering
    :return: `list` of all men older than `age`
    """
    result = []
    for p in people:
        if p.sex == 'man' and p.age > age:
            result.append(p)
    return result


def find(people, predicate):
    """
    Find all people given `predicate` function.

    :param people: `list` of people as instances of `Person`
    :param predicate: selector function with one argument that returns boolean value
    :return: `list` of all people that pass `predicate`
    """
    result = []
    for p in people:
        if predicate(p):
            result.append(p)
    return result

# Even more general is the `filter` function.
#
# def filter(iterable, predicate):
#     return (i for i in iterable if predicate(i))


if __name__ == '__main__':

    people = [Person('A', 33, 'man'), Person('B', 45, 'man'), Person('C', 12, 'man'), Person('D', 18, 'woman'),
              Person('E', 20, 'man'), Person('F', 73, 'man'), Person('G', 51, 'man'), Person('H', 33, 'woman'),
              Person('I', 16, 'man'), Person('J', 19, 'man'), Person('K', 27, 'man'), Person('L', 52, 'woman')]
    print(people)

    print('\nolder than 18:', find_older_than(people, 18))
    print('all men:', find_men(people))
    print('men older than 18', find_men_older_than(people, 18))

    print('\nusing abstract find:')
    print('older than 18:', find(people, lambda p: p.age > 18))
    print('all men:', find(people, lambda p: p.sex == 'man'))

    def emancipated_women(p):
        return p.sex == 'woman' and p.age > 20

    print('\nemancipated women:', find(people, emancipated_women))
