# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:42:00 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------

# assignment operation of twwo lists

# 1) shallow copy 
# 2) deep copy

# 📌🐍 -----------------------------------------------------------------------

# this is type of the normal copy 

l1 = [1,2,3,4]

l2 = l1

l1[0] = 10

print(l1)
print(l2)



# 📌🐍 -----------------------------------------------------------------------

# 1) shallow copy - 

l1 = [1,2,3,4]

l2 = l1.copy()

l1[0] = 10
print(l1)
print(l2)


# ---------------- or 


import copy 
l1 = [1,2,3,4,5]

l2 = copy.copy(l1)

l1[0] = 10
print(l1)
print(l2)




     # drawback of the shallow copy that it doesnt word two level deeper
     
import copy      
l1 = [[1,2,3,4],[5,6,7,8]]


l2 = copy.copy(l1)

l1[0][0] = 10

print(l1)
print(l2)



# Deep copy - 

import copy
l1 = [[1,2,3,4,5,6],[7,8,9,3,4]]

l2 = copy.deepcopy(l1)

l1[0][0] = 10
print(l1)
print(l2)

































