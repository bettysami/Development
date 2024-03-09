# name = input("What's your name? ")
# hello()
# print(name)

# Here is the error message What's your name? Betty
#Traceback (most recent call last):
 # File "C:\Cancode-practice\My Practice 3-8-2024\def.py", line 2, in <module>
   # hello()
  #  ^^^^^
# NameError: name 'hello' is not defined. Did you mean: 'help'?


#It s complaining because the hello function doesn't exist,so let's create/define the hello function


# def hello():
#     print("hello")   
# name = input("What's your name? ")



# hello()
# print(name)

# Let's parameterize the function above

# def hello():
#     print("hello,", to)   
# name = input("What's your name? ")
# hello(name)

#here is the error message : $ python def.py
#What's your name? betty
#Traceback (most recent call last):
#  File "C:\Cancode-practice\My Practice 3-8-2024\def.py", line 30, in <module>
 #   hello(name)
#TypeError: hello() takes 0 positional arguments but 1 was given


#here is my mistake : def hello(to)
def hello(to):
    print("hello,", to)   
name = input("What's your name? ")
hello(name)


