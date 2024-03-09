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


def hello():
....int("hello")   
name = input("What's your name? ")
hello()
print(name)