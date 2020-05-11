#Tuple
# A tuple is a collection which is ordered and unchangeable.
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)
'''
#You can access tuple items by referring to the index number,
# inside square brackets:
'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
'''
#Once a tuple is created, you cannot change its values.
#But there is a workaround
#You can convert the tuple into a list, change the list, and
# convert the list back into a tuple.
'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
'''
#You can loop through the tuple items by using a for loop.
'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
'''
#To determine if a specified item is present in a tuple use
# the in keyword:
'''
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
'''
#To determine how many items a tuple has, use the len() method:
'''
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
'''
#To create a tuple with only one item, you have to add a comma
# after the item,
'''
thistuple = ("apple",)
print(type(thistuple))
'''
#Tuples are unchangeable, so you cannot remove items from it,
# but you can delete the tuple completely:
'''
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
'''
#To join two or more tuples you can use the + operator:
'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
'''
#It is also possible to use the tuple() constructor to make a tuple.

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

#Python has two built-in methods that you can use on tuples.
'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''
