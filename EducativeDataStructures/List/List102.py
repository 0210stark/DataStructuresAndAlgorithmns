a_list = [2, 'Educative', 101]


def foo():
    print('Hello world from Foo!')


another_list = [a_list, 'Python', foo, ['Yet Another list']]
print(another_list[0])
print(another_list[0][1])
print(another_list[2])
print(another_list[3])

another_list[2]()
