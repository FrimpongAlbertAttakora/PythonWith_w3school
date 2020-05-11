#Collections (Arrays)
#There are four collection data types in the Python programming
#Language: List, Tuple, Set and Dictionary

#List:
# A list is a collection which is ordered and changeable.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#To change the value of a specific item, refer to the index number:
'''
thislist[1] = "blackcurrant"
print(thislist)
'''
#You can loop through the list items by using a for loop:
'''
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
'''
#To determine if a specified item is present in a list use
# the in keyword:
'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
'''
#To determine how many items a list has, use the len() function:
'''
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
'''
#To add an item to the end of the list, use the append() method:
'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
'''
#To add an item at the specified index, use the insert() method:
'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
'''
#There are several methods to remove items from a list:
#The remove() method removes the specified item:
'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#The pop() method removes the specified index, (or the
# last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
#The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
'''
#There are ways to make a copy.
'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#OR
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
'''
#There are several ways to join, or concatenate, two or more lists
'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#OR
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#OR
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
'''
#It is also possible to use the list() constructor to
# make a new list.
'''
thislist = list(("apple", "banana", "cherry"))
print(thislist)
'''
#List of Methods for List
'''
Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
'''