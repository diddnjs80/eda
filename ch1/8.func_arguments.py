# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:22:34 2019

@author: shkim
"""

"""
# 키워드 인수 (keyward arguments)
"""
#%%
def print_something(my_name, your_name):
    print("Hello %s, My name is %s" % (your_name, my_name))
    print("Hello {0}, My name is {1}".format(your_name, my_name))
    print("Hello {1}, My name is {0}".format(your_name, my_name))

print_something("kim", "lee")
print_something("lee", "kim")
print_something( your_name='Lee', my_name='Kim')



#%%
def kwargs_test( **kwargs ):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    print(kwargs['first'])


kwargs_test(first = 3, second = 4, third = 5)

#%%
def kwargs_test( **kwargs ):
    print(*kwargs)
   


kwargs_test(first = 3, second = 4, third = 5)

#%%
def kwargs_test( **kwargs ):
    print(kwargs)
    print("First value is {first}".format( **kwargs ))
    print("Second value is {second}".format( **kwargs ))
    print("Third value is {third}".format( **kwargs ))

kwargs_test(first = 3, second = 4, third = 5)
# kwargs_test(n1 = 3, n2 = 4, n3 = 5) #error

#%%
"""
# 디폴트 인수 (default arguments)
"""
#%%
def print_something(my_name, your_name='park'):
    print("Hello {}, My name is {}".format(your_name, my_name))

print_something("kim", "lee")
print_something("kim")




#%%
"""
# 가변 인수 (variable arguments)
"""
#%%
def vararg_test(a, b, c ):
    print(c)
    print(type(c))
    print(c[0])

vararg_test(1, 2, [3, 4, 5])  # 3,4,5
# print(vararg_test(1, 2, 3))  # 3,
# print(vararg_test(1, 2, 3,4))  # 3,4

#%%
def vararg_test(a, b, *c ):
    print(c)
    print(type(c))
    print(c[0])

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5
print(vararg_test(1, 2, 3))  # 3,
print(vararg_test(1, 2, 3,4))  # 3,4

#%%
def vararg_test(a, b, *args ):
    [*c] = args
    d = args
    print(args, c, d)
	c[1] = 44

print(vararg_test(1, 2, 3, 4, 5))  # 3,4,5



