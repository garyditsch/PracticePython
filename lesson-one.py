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

# Using variable within a string
# This requires using the format method which is f

first_name = 'Tony'
last_name = 'Stark'
full_name = f"{first_name} {last_name}"

print(full_name)

# adding some of these things together

favorite_heros = f"I like {super_hero2.title()} and {full_name}, but my favorite is {super_hero1.title()}."

print(favorite_heros)
