#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#In Python a function is defined using the def keyword:
'''
def my_function():
  print("Hello from a function")
'''
#To call a function, use the function name followed by parenthesis:
'''
my_function()
'''
#Information can be passed into functions as arguments.
'''
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
'''
#The terms parameter and argument can be used for the same thing:
# information that are passed into a function.
#A parameter is the variable listed inside the parentheses in the
# function definition.
#An argument is the value that is sent to the function when it is
# called.
#By default, a function must be called with the correct number of
# arguments.
#This function expects 2 arguments, and gets 2 arguments:
'''
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")
'''
#f the number of arguments is unknown, add a * before the
# parameter name:
'''
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
'''
#You can also send arguments with the key = value syntax.
'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
'''
#If the number of keyword arguments is unknown, add a double **
# before the parameter name:
'''
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
'''
#If we call the function without argument, it uses the default value:
'''
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
'''
'''
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
'''
#To let a function return a value, use the return statement:
'''
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
'''
#Pass statement
'''
def myfunction():
  pass
'''
#Python also accepts function recursion, which means a defined
# function can call itself.
'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)
'''


































































