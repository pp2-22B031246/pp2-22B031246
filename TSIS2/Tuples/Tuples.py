#Tuple example
mytuple = ("apple", "banana", "cherry")
""""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

"""
#Example 
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Tuple items
""""
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable
Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates
Since tuples are indexed, they can have items with the same value:

"""
#Example 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#Tuple length len()
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Create tuple with one item
""""
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

"""
#Example 
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items - data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#Example 
tuple1 = ("abc", 34, True, 40, "male")

#type()
""""
From Python's perspective, tuples are defined as objects with the data type 'tuple':

<class 'tuple'>
    """
#example 
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#The tuple() constructor  tuple()
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Python collections (arrays)
""""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

"""

