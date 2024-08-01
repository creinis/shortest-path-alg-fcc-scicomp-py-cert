# Shortest Path Algorithm
# the algorithm to calculate the shortest path between each node in your new graph.

# Step 1

#So far, you have already met different data types:

#    Immutable data types, such as integers, strings, tuples, and Booleans.
#    Mutable data types, such as lists.

#A dictionary is a mutable data type and it is identified by a pair of curly braces, {}.

#Start by creating a variable called copper and assign it an empty dictionary using a pair of curly braces, 
# in the same way you would create an empty list with a pair of square brackets.

copper = {}

# Step 2

# Dictionaries store data in the form of key-value pairs. 
# A key is separated from the correspondent value by a colon. 
# And each key-value pair is separated from the following pair by a comma:

my_dict = {
    'name': 'Michael',
    'occupation': 'Lumberjack'
}

# Add a new key-value pair to your dictionary. 
# Use the string species as the key, and the string guinea pig as the value.

copper = {'species': 'guinea pig'}

# Step 3

# Keys must be unique within a dictionary and they can be only immutable data types. 
# This means you cannot use a list or another dictionary as keys.

# Add another key age to your dictionary and give it the integer number 2 as value.

copper = {'species': 'guinea pig', 'age' : 2}

# Step 4

# You can access the data stored in a dictionary through its keys:

my_dict = {
    'name': 'Michael',
    'occupation': 'Lumberjack'
}

my_dict['name'] # 'Michael'

# After your dictionary, follow the example above to access the species key of copper and print the result.

copper = {
    'species': 'guinea pig',
    'age': 2
}
print(copper['species'])

# Step 5

# Now, modify your existing print() call to print the value of the age key.

# Step 6

#To add a new key-value pair after declaring a dictionary, 
# you can indicate the key in the same way you would access an existing key, 
# and set the value of the new key by using the assignment operator:

my_dict = {
    'name': 'Michael',
    'occupation': 'Lumberjack'
}

my_dict['country'] = 'Canada'

# Delete your print() call. Then, after declaring copper, add the key food to your dictionary 
# and set its value to hay.

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'

# Step 7

#Now, at the bottom of your code, print copper.

# Step 8

# The same syntax can be used to change the value of an existing key.
# Just before the print() call, access the species key and reassign its value to Cavia porcellus

copper = {
    'species': 'guinea pig',
    'age': 2
}
copper['food'] = 'hay'
copper['species'] = 'Cavia porcellus'
print(copper)


