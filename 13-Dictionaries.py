#Dictionaries
#A dictionary is a collection which is unordered, changeable
# and indexed.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#Get the value of the "model" key:
'''
x = thisdict["model"]
print(x)
'''
#There is also a method called get() that will give you
# the same result:
'''
x = thisdict.get("model")
print(x)
'''
#You can change the value of a specific item by
# referring to its key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
'''
thisdict["year"] = 2018
print(thisdict.get("year"))
'''
#Print all key names in the dictionary, one by one:
'''
for x in thisdict:
  print(x)
'''
#Print all values in the dictionary, one by one:
'''
for x in thisdict:
  print(thisdict[x])
'''
#You can also use the values() method to return values
# of a dictionary:
'''
for x in thisdict.values():
  print(x)
'''
#Loop through both keys and values, by using the items() method:
'''
for x, y in thisdict.items():
  print(x, y)
'''
#Check if "model" is present in the dictionary:
'''
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
'''
#To determine how many items (key-value pairs) a dictionary has,
# use the len() function
#print(len(thisdict))
#Adding an item to the dictionary is done by using a new index key
# and assigning a value to it:
'''
thisdict["color"] = "red"
print(thisdict)
'''
#Removing Items
#The pop() method removes the item with the specified key name:
'''
thisdict.pop("model")
print(thisdict)
'''
#The popitem() method removes the last inserted item
'''
thisdict.popitem()
print(thisdict)
'''
#The del keyword removes the item with the specified key name:
'''
del thisdict["model"]
print(thisdict)
'''
#The del keyword can also delete the dictionary completely:
# del thisdict
#The clear() method empties the dictionary:
'''
thisdict.clear()
print(thisdict)
'''
#One way to make a copy is to use the built-in Dictionary method
# copy().
'''
mydict = thisdict.copy()
print(mydict)
'''
#Another way to make a copy is to use the built-in function dict().
'''
mydict = dict(thisdict)
print(mydict)
'''
#A dictionary can also contain many dictionaries, this is called
# nested dictionaries.
'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
'''
'''
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily.get("child1").get("name"))
'''
#It is also possible to use the dict() constructor to make
# a new dictionary:
'''
thisdict = dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
'''
#Python has a set of built-in methods that you can use
# on dictionaries.
'''
Method	Description
clear() Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()  Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()   Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''