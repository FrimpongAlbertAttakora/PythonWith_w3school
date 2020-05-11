#Python has two primitive loop commands:while loops and for loops
#With the while loop we can execute a set of statements as long
# as a condition is true.
'''
i = 1
while i < 6:
  print(i)
  i += 1
'''
#With the break statement we can stop the loop even if the while
# condition is true:
'''
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
'''
#With the continue statement we can stop the current iteration,
# and continue with the next:
'''
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
'''
#With the else statement we can run a block of code once when
# the condition no longer is true:
'''
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
'''

#A for loop is used for iterating over a sequence (that is either
# a list, a tuple, a dictionary, a set, or a string).
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''
#
#Even strings are iterable objects, they contain a sequence of
# characters:
'''
for x in "banana":
  print(x)
'''
#With the break statement we can stop the loop before it has looped
# through all the items:
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
'''
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
'''
#To loop through a set of code a specified number of times, we can
# use the range() function,
'''
for x in range(6):
  print(x)
'''
#Using the start parameter:
'''
for x in range(2, 6):
  print(x)
'''
#Increment the sequence with 3 (default is 1):
'''
for x in range(2, 30, 3):
  print(x)
'''
#The else keyword in a for loop specifies a block of code to
# be executed when the loop is finished:
'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")
'''
#A nested loop is a loop inside a loop.
'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)
'''
#for loops cannot be empty, but if you for some reason have a for
# loop with no content, put in the pass statement to avoid getting
# an error.
'''
for x in [0, 1, 2]:
  pass
'''




















































