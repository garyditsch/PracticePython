"""
Learning:
1. use python in the terminal
2. how to create a variable
3. what is a string
4. what are some methods available for string manipulation

"""



# printing a message
print('Hello everyone, this is printing in python')

# create a variable
myMessage = 'Saying Hello World'

print(myMessage)


# string data type in python is between quotes, single or double
string_1 = 'This is an example of a string'
string_2 = "This is also a string type"

print(string_1)
print(string_2)

# python offers many methods that can be used on strings
# .title()
# .upper()
# .lower()
## here are a few examples which we will use after creating a string


super_hero1 = 'spiderman'
super_hero2 = 'The hulk'

print(super_hero1)
print(super_hero1.title())
print(super_hero1.upper())
print(super_hero1.lower())

print(super_hero2)
print(super_hero2.title())
print(super_hero2.upper())
print(super_hero2.lower())

# Using a variable within a string
# This requires using an f-string (or formatted string literals)

# Lets create our string variables
super_hero1 = 'spiderman'
super_hero2 = 'The hulk'
first_name = 'tony'
last_name = 'stark'

# Here I am going to just create a new variable using first and last name
# I am also making sure the names are capitalized using the title method
full_name = first_name + ' ' + last_name
print(full_name.title())

# adding some of these things together
favorite_heros = f"I like {super_hero2.title()}, but my favorite is {super_hero1.title()}."
print(favorite_heros)

# dealing with white space in a string
# .rstrip()
# .lstrip()
# .strip()

movie_favorite = ' Guardians of the Galaxy '

# print variable as it was written spaces before, after and in the middle
print(movie_favorite)

# remove the space before Guardians
print(movie_favorite.lstrip())

# remove the space after Galaxy
print(movie_favorite.rstrip())

# remove both spaces
print(movie_favorite.strip())

# prove that space was removed after Galaxy

print(f"{movie_favorite.strip()},{full_name}")
