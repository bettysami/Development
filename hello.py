#print("hello,world") # here print is the function, "hello,world is the argument to the function"

#let's add a bug
#print("hello," # SyntaxError: '(' was never closed
      
# let's correct the bug
#print("hello,world")

# introduce input
#print("what's your name? ") 
#input("what's your name? ")
#print("hello,world")    

# let's fix the above
# input("what's your name? ")
# print("hello,Betty")  


# Return values
# Let's learn about return values

#variables : A variable is a container of values inside of a computer
#name = input("what's your name? ") #Hre the variable is "name"
#print("hello, name")

#let's fix the above
#name = input("what's your name? ")
#print("hello")
#print(name)

# Comments: Comments are notes to yourself in the code, they stars with #

# Ask user for their name
#name = input("what's your name? ")

#Say hello to user
#print("hello")
#print(name)

# pseudocode : it's a good way of structuring your to do list, it breaks a big problem down into small tasks
# Ask user for their name


# Say hello to user

# let's try pseudocode
# Ask user for their name
#name = input("What's your name? ")

# Say hello to user
#print("hello")
#print(name)

"""
Is a another way of doing multi-comment

"""

# Let's improve our code
#name = input("what's your name? ")
#print("hello, " + name)  # here I made use of + to add two strings together

# Let's improve our code
#name = input("what's your name? ")
#print("hello,", name) # let's remove the operator +

# Let's introduce "str" str short for string is a type of data in a program
# functions take arguments to influence their behavior
# check the documentation for python str functions in "docs.python.org/3/library/functions.html#print"

# Let's fix the presentation of the output above

# name = input("what's your name? ")
# print("hello, ", end="")
# print(name)

# name = input("what's your name? ")
# print("hello, ", end="???")
# print(name)

# name = input("what's your name? ")
# print("hello, ", name)

# name = input("what's your name? ")
# print("hello, ", name, sep="???")

#Let's try quotations inside quotation
# print("hello, \"friend\"")


#Let's try {}
# name = input("what's your name? ")
# print("hello,{name}")

#Let's format the above
# name = input("what's your name? ")
# print(f"hello, {name}") # The f will format the output of print



#Parameters: Named parameters e.g end, 