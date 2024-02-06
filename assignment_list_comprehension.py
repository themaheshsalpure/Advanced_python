# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:55:09 2023

@author: ASUS
"""

# 📌🐍 -----------------------------------------------------------------------    


# find all the numbers from 1 to 1000 that are divisible by 7

lst = [num for num in range(1,1000) if num%7==0]
print(lst)


# 📌🐍 -----------------------------------------------------------------------    


# find all the numbers from 1 to 1000 that have 3 in them 

lst = [num for num in range(1,1000) if num%10 == 3]
print(lst)


# 📌🐍 -----------------------------------------------------------------------    


# finding all the numbers from 1 to 1000 that having 5 in it

lst1 = [ n for n in range(1,1000) if n%10 == 5]
print(lst1)


# 📌🐍 -----------------------------------------------------------------------    


# counting the number of spaces present in the given string 

# logic 1 -
str1 = 'Hello my name is mahesh'
count = 0

for i in str1:
    if i == ' ':
        count += 1

print(count)


# logic 2 -
str1 = 'hello my name is mahesh'
count = 0

for i in range(len(str1)):
    if str1[i]==' ':
        count+=1
print(count)

# logic 3 -

str1 = 'hello my name is mahesh'

list1 = [n for n in str1 if n == ' ']
print(len(list1))


# 📌🐍 -----------------------------------------------------------------------    


# create a list of consonents in the string 

sentence='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

l1  = ['a','e','i','o','u']
l2 = []

for i in sentence:
    if i not in l1:
       l2.append(i)
print(l2)



sentence='Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams'

l1  = ['a','e','i','o','u']
lst = [n for n in sentence if n not in l1 ]
print(lst)



# 📌🐍 -----------------------------------------------------------------------    

# finding common number in two lists without using list and tuples

lst1=[1,2,3,4]
lst2=[2,3,4,5]

lst = [num for num in lst1 if num in lst2]
print(lst)
       

       
# 📌🐍 -----------------------------------------------------------------------    
       

string1='In 1980 there were 13 instances of a protest with over 1000 1st'
word = string1.split()

lst1 = [x for x in word if not x.isalpha()]   # x.isalpha() checks that it is an alphabate or not
print(lst1)




# 📌🐍 -----------------------------------------------------------------------    


# print 'even' if the number is even and vice verssa for the numbers upto 20


lst = ['even' if num%2 == 0 else 'odd' for num in range(20)]
print(lst)

# 📌🐍 -----------------------------------------------------------------------    


# produce a list of tuples consisting of only the matching numbers in the lists

lst1=[1,2,3,4,5,6,7]
lst2=[1,2,3,4,5,6,7]
lst3=[(x,y)for x in lst1 for y in lst2 if x==y ]
print(lst3)


# 📌🐍 -----------------------------------------------------------------------    

# find all the word in a string that are less 4 letter 

# using normal method
sentence='On a summer day ramnath sonar went swimming in the sun and his red skin stung'
l = []

words = sentence.split()
for word in words:
    if len(word) < 4:
     l.append(word)
     
print(l)


# using list comprehension
sentence='On a summer day ramnath sonar went swimming in the sun and his red skin stung'
words = sentence.split()

l = [word for word in words if len(word)<4 ]
print(l)


# 📌🐍 -----------------------------------------------------------------------    

#write python program to print a specified list 
#after removing 0th 4th and 5th element


color=['red','black','white','blue','voilet','green']
lst1=[x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(lst1)


# 📌🐍 -----------------------------------------------------------------------    


#write python program that create generator function 
# that yeilds the cube of number from 1 to n(user defined value)


def cube(n):                      #100
    for i in range(1,n+1):        # this will run from 1 to 100
        yield i**3                # i^3
        
                                  #generator is created i.e object is craeted
     
cubes=cube(100)                   # we have pass 100 as a agrument to the cube function

for i in cubes:                   # this will take object and print it
    print(i)
    
next(cubes)                       # this take object one by one




def cube(num):
    for i in range(1,num+1):
        yield i**3
        
cubes = cube(100)

for i in cubes:
    print(i)



# 📌🐍 -----------------------------------------------------------------------    


# write python program generate generator from given range

import random

start=int(input('Enter the start number: '))

end=int(input('Enter the end number: '))
def random_num_generator(start,end):
    n=0
    while n<=end:
        yield random.randint(start,end)
        n+=1
        
random_num=random_num_generator(start,end)

for i in random_num:
    print(i)


3

import random

def random_int(start,end):
    n = 0
    while  n <= end:
        yield random.randint(start, end)
        n+=1


random_num = random_int(1, 50)

for i in random_num:
    print(i)
        
        
































