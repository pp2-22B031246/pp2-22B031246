#Access items
""""
You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""
#Example 
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
  
  #Example 
  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Change items
#Once a set is created, you cannot change its items, but you can add new items.
