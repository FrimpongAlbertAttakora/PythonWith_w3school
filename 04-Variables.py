#VARIABLES
#In Python, variables are created when you assign a value to it:
#Unlike other programming languages, Python has no command
# for declaring a variable.
'''
x = 5
y = "Hello, World!"
print(y)
'''
# Variables can change types after they have been set
'''
x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)
'''
# String variables can be declared either by using
# single or double quotes:
'''
x = "John"
# is the same as
x = 'John'
'''
#A variable name must start with a letter or the underscore
# character and it is case sensitive eg. age, Age and AGE
# are three different variables
#Legal variable names:
'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''
#Python allows you to assign values to multiple variables in one line:
'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
'''
#you can assign the same value to multiple variables in one line:
'''
x = y = z = "Orange"
print(x)
print(y)
print(z)
'''
#To combine both text and a variable, Python uses the + character:
'''
x = "Python is "
y = "awesome"
z =  x + y
print(z)
'''
'''
x = 5
y = 10
print(x + y)
'''
#Global and local variables
'''
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
'''
'''
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
'''
#If you use the global keyword, the variable belongs to the global scope:
'''
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
'''

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
  print(x)
myfunc()
print("Python is " + x)
