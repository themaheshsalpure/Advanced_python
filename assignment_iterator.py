# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 15:36:31 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------

'''
write python program to create iterator from the several iterables ina  sequence and display the 
type and elements of the new iterator

'''

# for lists

from itertools import chain

l1 = [1,2,3,4]
l2 = ['a','b','c','d']
l3 = [6,7,8,9]


def iterator_1(l1,l2,l3):
    return chain(l1,l2,l3)

results = iterator_1(l1, l2, l3)
print(results)
print(type(results))

print('The elements of the lists are : \n')
for i in results:
    print(i)


# for tuples 

from itertools import chain

l1 = (1,2,3,4)
l2 = ('a','b','c','d')
l3 = (6,7,8,9)


def iterator_1(l1,l2,l3):
    return chain(l1,l2,l3)

results = iterator_1(l1, l2, l3)
print(results)
print(type(results))

print('The elements of the lists are : \n')
for i in results:
    print(i)




# write a python that generates the running product of iterables


from itertools import accumulate
import operator

l = [1,2,3,4,5]
def running_product(l):
    return accumulate(l,operator.mul)

## if we doesnt give any argument to the operator then it takes addition as the default arg

result = running_product(l)
for i in result:
    print(i)





from itertools import accumulate
import operator

l = (1,2,3,4,5,6)

def info(l):
    return accumulate(l,)



# 📌🐍 -----------------------------------------------------------------------

'''

python program to construct an infinite iterator that returns evenly spaced values 
starting with a specified number and step

'''
# firsst we will assign the start and the step of number 
import itertools as it
start = 10
step = 1

# this will create the infinite loop of numbers 
counter = it.count(start,step)

# this will read the data from the counter and print it one by one 
for i in counter :
    print(i)

# 📌🐍 -----------------------------------------------------------------------

'''
write python program to generate an infinite cycle of elements from an iterable

'''
       # this will create a cycle of the elements which cycle will run infinite 

from itertools import cycle


l = [1,2,3,4,5]

       # cycle() is used to create an cycle where the elements of the list will 
       # be printed continuously  infinite times
info = cycle(l)
for i in info:
    print(i)

    # using string for the cycle data 

str1 = 'hello world'

result = cycle(str1)
for i in result:
    print(i)


# 📌🐍 -----------------------------------------------------------------------

'''
write a python program to make an iterator that drops elements from the iterables as soon as 
an element is a positive number 

'''


import itertools as it

num = [-2,-3,4,6,-4,-5,-6,7,8]

def drop_while(num):
    
    # it.dropwhile() will drop the items till the first positive number occurs 
    return it.dropwhile(lambda x: x < 0, num)

results = drop_while(num)

print(list(results))



















