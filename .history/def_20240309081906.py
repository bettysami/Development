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
# def hello(to):
#     print("hello,", to)   
# name = input("What's your name? ")
# hello(name)


#Let's ay hello to specific person or the world
# def hello(to="world"):
#     print("hello,", to)   

# hello()
# name = input("What's your name? ")
# hello(name)


# let's say we don't wamt to use " hello" all te time

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)   # nothing happened when I typed in the terminal python def.py , let's fix this

# let's fix it
def main():
    name = input("What's your name? ")
    hello()

def hello():
    print("hello,", name)

main()    # this return the error message  
#  python def.py
# What's your name? betty
# Traceback (most recent call last):
#   File "C:\Cancode-practice\My Practice 3-8-2024\def.py", line 73, in <module>
#     main()    
#     ^^^^^^
#   File "C:\Cancode-practice\My Practice 3-8-2024\def.py", line 68, in main
#     hello()
#   File "C:\Cancode-practice\My Practice 3-8-2024\def.py", line 71, in hello
#     print("hello,", name)
#                     ^^^^
# NameError: name 'name' is not defined

Let's fix it, to see the fix, go to 