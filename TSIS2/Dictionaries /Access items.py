#Accessing items
#You can access the items of a dictionary by referring to its key name, inside square brackets:
#Example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#There is also a method called get() that will give you the same result:
#Example 
x = thisdict.get("model")


#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
#Example 
x = thisdict.keys()

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
#Example 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


#Get Values 
#The values() method will return a list of all the values in the dictionary.
#Example 
x = thisdict.values()


#The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
#Example 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


#Example 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.
#example 
x = thisdict.items()

#The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
#Example 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


#Example 
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change


#Check if Key exist
#To determine if a specified key is present in a dictionary use the in keyword:
#Example 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")