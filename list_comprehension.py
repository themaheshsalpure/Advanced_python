# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:25:44 2023

@author: ASUS
"""

l = []
for num in range(0,20):
    l.append(num)
    
print(l)



lst = [num for num in range(0,20)]
print(lst)


# 📌🐍 -----------------------------------------------------------------------    

l1 = ['mahesh', 'yuvraj', 'akshay']

l2 = [name.capitalize() for name in l1]
print(l2)


# 📌🐍 -----------------------------------------------------------------------    

# even - odd number codde in list-comprehension
# if the given number is even then it will be appended on the lst

def is_even(num):
    return num%2 == 0


lst = [
       num
       for num in range(10)
       if is_even(num)
       ]


print(lst)

# 📌🐍 -----------------------------------------------------------------------    


# using the nested for loop or two for loops 

lst = [f'{x}{y}' for x in range(3) for y in range(3)]
print(lst)



# 📌🐍 -----------------------------------------------------------------------    





def value():
    for i in range(1,10):
        yield i

for i in value():
    print(i)




