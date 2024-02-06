# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:25:35 2023

@author: ASUS
"""


# 📌🐍 -----------------------------------------------------------------------

# zip function is used to combine the two list values with respect to their indexes


name = ['dada','mama','kaka']
info = [4005,5637,9253]

for nm, inf in zip(name,info):
    print(nm,inf)
    
    
# 📌🐍 -----------------------------------------------------------------------

name = ['dada','mama','kaka','baba']
info = [4005,5637,9253]

for a, b in zip(name,info):
    print(a,b)
    

    
# 📌🐍 -----------------------------------------------------------------------


# zip_longest function
# this will asign the none value at the end of string where the lenght of both string doesnt match

from itertools import zip_longest
name = ['dada','mama','kaka','baba']
info = [4005,5637,9253]

for nm, inf in zip_longest(name,info):
    print(nm,inf)
    
    
# 📌🐍 -----------------------------------------------------------------------

# fillvalue=0 will replace the none value with the 0 

from itertools import zip_longest

name = ['dada','mama','kaka','baba']
info = [4005,5637,9253]


for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)


# 📌🐍 -----------------------------------------------------------------------\
    

#all() checks the all the items in the list are positive are not 

lst = [1,2,3,4,0]

if all(lst):
    print("All are true")
    
else :
    print("false")



# any() checks that any one non zero value prresent in the list or not

lst = [0,0,0,0,0]

if any(lst):
    print('available positive')
else :
    print('negative')


# 📌🐍 -----------------------------------------------------------------------

from itertools import count

counter = count()            # here counter starts from 0 

print(next(counter))
print(next(counter))
print(next(counter))



from itertools import count

counter = count(start= 1)            # starting counter from 1

print(next(counter))
print(next(counter))
print(next(counter))



# 📌🐍 -----------------------------------------------------------------------

# cycle() method will continue the loop infinite times for iterating through the list

from itertools import cycle

l = ['mahesh','yuvraj','shrikant','chetan']

for i in cycle(l):
    print(i)



# 📌🐍 -----------------------------------------------------------------------

# repeat() will reppeat the given message 4 times 
from itertools import repeat


for msg in repeat('keep calm',times=4):
    print(msg)



# 📌🐍 -----------------------------------------------------------------------




from itertools import combinations

l = ['mahesh','shrikant','yuvraj','chetan']

for i in combinations(l, 2):
    print(i)




from itertools import permutations

l = ['mahesh','shrikant','yuvraj','chetan']

for i in permutations(l, 2):
    print(i)


# 📌🐍 -----------------------------------------------------------------------


# product() method
from itertools import product

l = ['mahesh','shrikant','yuvraj','chetan']

for i in product(l):
    print(i)





  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  