# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 09:59:18 2023

@author: ASUS
"""

# uses keyword = 'yeild'

# generators implemented using function

# 📌🐍 -----------------------------------------------------------------------    


gen = (
       x
       for x in range(20)
       )
print(gen)

for num in gen:
    print(num)
    
    
    # method to access the values in next(gen)
    
    
gen = (
    x
    for x in range(3)
    )
next(gen)
next(gen)



# 📌🐍 -----------------------------------------------------------------------    

def is_even(end):
    for num in range(0,end,2):
        yield num
        
        
for num in is_even(6):
    print(num)



# using next(gen) function

def is_even(end):
    for num in range(0,end,2):
        yield num
        
        
gen = is_even(6)
next(gen)
next(gen)




# 📌🐍 -----------------------------------------------------------------------    

# replacing the password with the * to hide the password
def length(example):
    for x in example:
        yield len(x)
        
def hide(example):
    for x in example:

        yield x*'*'
        
        
password = ['mahesh_s','Mahesh171_','mAhesh_231_/']

for i in hide(length(password)):
    print(i)

# 📌🐍 -----------------------------------------------------------------------    

# printing the list items with their index
lst = ['milk','starch','apple']
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')



lst = ['milk','starch','apple']

for index, items in enumerate(lst, start=1):
    print(f'{index} {item}')



