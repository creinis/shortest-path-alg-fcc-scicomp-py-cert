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


