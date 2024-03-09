# ask user their name
# name = input("what's your name? ")

# # Remove Whitespace from str
# name = name.strip()

# # Capitalize user's name
# name = name.title()

# # Say hello to user
# print(f"hello, {name}")

#But the above capitalizes only the first word, let's fix it with title function, I just replaced capitalize function with title function
# This is too much line of code let's reduce the lins of code

# ask user their name
name = input("what's your name? ")

# Remove Whitespace from str
name = name.strip().title

# Capitalize user's name
name = name.title()

# Say hello to user
print(f"hello, {name}")