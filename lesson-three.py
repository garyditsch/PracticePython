"""
Learning:
1. What lists are in python 
2. How to target an item in a list
3. Methods that can be utilized to manipulate lists: sort(), append(), remove()

"""

shoes = ['Nike', 'Adidas', 'Hoka', 'Sketchers', 'New Balance', 'Asics']
print(shoes)

# lists are indexed and you can get an item off the list using that index
# the one gotcha with that index is that it starts at 0
# this means to get the first item you use the index of 0

print('This is the first shoe in the list: ', shoes[0])
print('This is the last shoe in the list: ', shoes[5])

# The only issue with getting the last item this way is that we are getting a specific index number
# We do not always know how long a list will be therefore we can do the following

print('This is the last shoe in the list: ', shoes[-1])

# We can also get the length of a list, which would give us another way to get the last item

listLength = len(shoes)
print('The length of the list: ', listLength)

print('The last item on the list: ', shoes[listLength - 1])

# Notice we had to subtract 1 from the length, because the index started at zero
# If we did not do that, we would get an index error because the index would be 1 greater than exists on the list

# print(shoes[listLength])  --> This does not work

# When we have a list, we often want to manipulate and organize those items
# There are some methods in python had can help us with those efforts
# https://www.w3schools.com/python/python_lists_methods.asp

# Sort a list alphabetically
print('I have not sorted the list yet: ', shoes )
shoes.sort()

print('It is now sorted alphabetically: ', shoes)

# Sometimes we want to sort in descending order, we can pass the reverse argument and set it to true
shoes.sort(reverse=True)
print('The list is now sorted in descending alpha', shoes)

# It is also possible to write your own function to determine how to do the sort, but we'll do that when we learn functions

# There are times we want to add and remove items from a list
# append() will allow us to add
# remove() will allow us to remove
# let's try both

shoes.append('Crocks')
print('The list should now have Crocks: ', shoes)

# Notice the item was added as the last item on the list

shoes.remove('Adidas')
print('The list should now have Adidas removed: ', shoes)

# Lets add Adidas back
shoes.append('Adidas')
print('We should see Adidas again: ', shoes)

# We now have a couple things to pay attention to now that we've added Adidas back
# The list is no longer sorted because we've added Adidas and it's at the end of the list

# Also, what would happen if we tried added multiple items with the same name 
# Or, what happens if we have two items with the same name and remove it
# Let's try

# Add Adidas one more time
shoes.append('Adidas')
print('We should now see Adidas on the list twice, both at the end: ', shoes)

# Yes... it is all working
# Now, let's remove it

shoes.remove('Adidas')
print('What happens to our list here? ', shoes)

#hmm, we still have one Adidas. That is because remove will only remove the first occassion that it encounters the value

# There are many other things to do with the methods available for lists, check out these resources and try some on your own


