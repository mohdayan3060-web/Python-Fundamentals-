# # ValueError: The type is right, but the value is wrong. (e.g., Passing the string "hello" to int(). It accepts strings, but it cannot convert letters).TypeError: The type itself is completely wrong. (e.g., Trying to add a string to a number like "apple" + 5).
# x=20
# print(id(x))

# # Dynamic Typing: The object has a type, not the variable name. You can reassign the "sticky note" to a completely different type of object.
# # The id() function: This reveals the memory address of an object. Let's prove dynamic typing:

# user_id=id(x)
# print(user_id)

# # Question 1A: The f-String Formatter
# # Write a program that asks the user for:
# # An item name (e.g., "Laptop")
# laptop=input("Which barnd laptop you want to buy ")
# # The price of the item (e.g., 1200.50)
# price=int(input("Enter the price of laptop"))

# # The quantity they want to buy (e.g., 2)
# qty=int(input("Enter the quntity of the "))
# # Calculate the total cost. Then, use a single print() statement with an f-string to output:
# total=price *qty
# print(f"your laptop beleong to this brand {laptop} and price is {price} and the quantity is :{qty} and Total amount you want to pay is {total}")

# # Question 1B: The Memory Detective
# # Write a short script that does the following:
# # Assigns the value 100 to a variable named num1.
# num01=100

# # Assigns the variable num1 to a new variable named num2 (i.e., num2 = num1).
# num2=num01
# # Prints the id() of both num1 and num2. Are they the same? Why?
# print(id(num01))
# print(id(num2))
# # Reassign num1 to 200.
# num1=200

# # Print the id() of num1 and num2 again. Print the values of both. Explain what happened to num2.
# print(id(num01))
# print(id(num2))
# # cheking the key words in python 
# import keyword

# print(keyword.kwlist)


# python string 
# text = "Python123"
# The word "Programming"
# print(text[6:17])
# Every second character of the entire string (e.g., "Pto... ")
# print(text[::2])
# The string completely reversed.
# print(len(text))
# print(text[::-1])
# print(text.capitalize())
# print(text.lower())
# print(text.upper())
# print(text.swapcase())
# print(text.center(100))
# print(text.count("x"))
# print("hello new {}".format(text))
# print(text.isalnum())
# print(text.isdigit())

raw_data = " Name: JOHN_DOE_123 ; Age: 25 "
# print(raw_data)
# print(raw_data.strip())
# print(raw_data.replace("25","21"))
# print(raw_data.lower())
# print(raw_data.split("---"),raw_data.lower(),raw_data.strip())
# -------------------------------------------------------------------------------------------------------------------

# List is a built-in data structure used to store an ordered collection of items. They are dynamic, resizable and capable of storing multiple data types.

# Mutable: list elements can be changed, updated, added, or removed after the list is created.
# Ordered: elements maintain the order in which they are inserted.
# Index-based: elements are accessed using their position, starting from index 0.
# a = ["faiz",1, 2, 3]
# print(a)

# b = ["apple", "banana",True,False,3.12,0]
# print(b)
# a.append("ayan")
# a.insert(2,"khan")


# res=a+b

# # a.append("ayan")
# print(res)