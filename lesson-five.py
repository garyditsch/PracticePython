"""
Learning:
1. Intro to tuples 
2. Creating a tuple with 1 item
3. What data types can be stored in a tuple
4. Can we iterate over tuples?

"""

# The biggest difference between a tuple and a list is that
# a tuple is immutable (it can not be changed)

# Let's create a tuple

first_tuple = ('Nebraska', 'Kentucky', 'Colorado', 'Florida', 'Iowa', 'Texas')
print('1', first_tuple)

# Like a list we can get items off by using the index

print('1', first_tuple[0])
print('1', first_tuple[1])

# Now let us try and change an item in the tuple

# first_tuple[3] = 'New Mexico'

# Notice that we get an error
# Now go back and comment line 24 out, so we can move on!
# What about creating a tuple with only one item

second_tuple = ('Lexington')
print('2', second_tuple)

# That appears to have worked but let us print out the type that our variable is
# We can do this using the type function
print('2', type(second_tuple))

# Ah, notice we get <class 'str'>
# Let us try again

third_tuple = ('Boulder', )
print('3', type(third_tuple))

# Now that we've added the comma after our first item, we get back
# <class 'tuple'>

# What data types can we use?
# Let's first try integers

fourth_tuple = (1,2,3,4,6,7,8)
print('4', fourth_tuple)

# That works, now let us try and mix different data types
# Let's try a integer, string, boolean and float)

fifth_tuple = ('Lincoln', 1, True, 3.0)
print('5', fifth_tuple)

# Last thing about tuples for now
# Can we iterate over them?

for state in first_tuple:
    print(state)

# Success, we get all the states listed in our first tuple





