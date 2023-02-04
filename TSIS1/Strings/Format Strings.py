#String Format 
#Not correct example (As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:)
age = 36
txt = "My name is John, I am " + age
print(txt)

#Example 
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Example 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#Example 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))