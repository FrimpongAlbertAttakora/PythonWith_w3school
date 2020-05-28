#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.
'''
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)
'''
#All classes have a function called __init__(), which is always executed when the
# class is being initiated.
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
'''
#Objects can also contain methods. Methods in objects are functions that belong to the object.
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()
'''
'''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
'''
#You can modify properties on objects like this:
'''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my age is " + abc.age)
p1 = Person("John", 36)
p1.age = 40
print(p1.age)
'''
#You can delete properties on objects by using the del keyword:
#del p1.age












































