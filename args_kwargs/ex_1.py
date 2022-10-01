#!/usr/bin/python3

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg throug *argv: ", arg)

def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print("{} == {}".format(key, value))

def pass_args(arg1, arg2, arg3):
    print('arg1: {}'.format(arg1))
    print('arg2: {}'.format(arg2))
    print('arg3: {}'.format(arg3))

args = ('two', 2, 3)
kwargs ={'arg1': 3, 'arg2': 'four', 'arg3': 7}

pass_args(**kwargs)
print('----------')
pass_args(*args)

print('----------')
greet_me(name = 'koby', age = 34)

print('----------')
test_var_args('boy', 'cat', 'hen', 'eggs')
