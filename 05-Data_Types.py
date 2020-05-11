#Data Types
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
'''
#You can get the data type of any object by using the type() function:
'''
#Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))
'''
'''
x = 35e3
y = 12E4
z = -87.7e100
print(x)
print(type(y))
print(type(z))
'''
'''
x = 3+5j
y = 5j
z = -5j
print(x)
print(type(x))
print(type(y))
print(type(z))
'''
#Convert from one type to another:
'''
x = 1 # int
y = 2.8 # float
z = 1j # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))
'''
#Random Number
#Import the random module, and display a random number between 1 and 9:

import random
print(random.randrange(1,10))