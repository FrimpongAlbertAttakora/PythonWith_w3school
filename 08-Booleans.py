#Boolean
#Booleans represent one of two values: True or False
'''
print(10 > 9)
print(10 == 9)
print(10 < 9)
'''
#When you run a condition in an if statement, Python returns
# True or False:
'''
a, b = 200, 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
'''
'''
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
'''
#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
'''
bool("abc")
bool(123)
print(bool(["apple", "cherry", "banana"]))
bool(False)
bool(None)
bool(0)
bool("")
print(bool(()))
bool([])
bool({})
'''
#You can create functions that returns a Boolean Value:
'''
def myFunction() :
  return True
print(myFunction())
'''
#You can execute code based on the Boolean answer of a function:
'''
def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")
'''
#Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
