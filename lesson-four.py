"""
Learning:
1. Continued lists 
2. Getting slices of a list
3. Looping through lists

"""

# Create the list
cfb = ['Huskers', 'Wildcats', 'Tigers', 'Wolverines', 'Hawkeyes']
print('The teams: ', cfb)

# Get the first three teams from the list
print(cfb[0:3])

# Notice that we give a starting index 0, and an ending index 3
# Also notice that the item with the ending index (3) is not included in our list

# Get the 3rd, 4th and 5th teams
print(cfb[2:5])

# This works because we know how long the list is with 5 teams
# we could use the len() method to get the length and use that answer also
# but we have an easier solution in python

print(cfb[2:])

# Notice the result is the same as line 20
# If we leave the index off after the semi-colon, python assumes that it goes until the end of the list

print(cfb[:3])

# The same works if we leave the index off prior to the semi-colon
# Python assumes that we start at the beginning of the list

# This allows us to create a copy of a list if we wanted in the following manner

newList = cfb[:]
print(newList)

# We can manipulate the new list but maintain the original. 
# Let's add another team to the new list to test this

newList.append('Gamecocks')
print('The new list that has been changed: ', newList)

print('The original list', cfb)

# But what if we want do things with our list
# For example, what if I wanted to print a sentence with every team inserted into it?

# We have loops! Which are used commonly for many different reasons in programming
# Primarily, so we can repeat an action many times and only write the code once
# Here is a simple example

for team in cfb: 
    print('The', team, 'are the best team in college football!')

# A couple things to notice
# 1. the for loop loops through every item in the list
# 2. each time the 'team' is the next item and can be accessed in the body of the loop
# 3. the indentation is critical! in python, it is the indetation that indicates that the line is within the for loop
# 4. the use of the word 'team' is not required, in fact it could be whatever variable I name it
# 5. it is best practice to use single and plural words for exame this would probably be better as
#   for team in teams: 

for x in cfb: 
    print(x)

# This is just to highlight that teams is not required and instead I named that variable x

# We can use our knowledge of slicing from above to only loop through the first three as follows

for team in cfb[:3]:
    print('The', team, 'are one of the top three teams')

