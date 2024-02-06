# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:29:51 2023

@author: ASUS
"""
# 📌🐍 -----------------------------------------------------------------------

age = [27,17,21,19]

adults = filter(lambda age: age>=18,age) 
print([age for age in adults])                     # list comprehension used here 


# 📌🐍 -----------------------------------------------------------------------