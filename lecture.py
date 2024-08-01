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

# Step 9

# You can remove a key-value pair from a dictionary by using the del keyword. The syntax is the following:

my_dict = {
    'name': 'Michael',
    'occupation': 'Lumberjack'
}

del my_dict['occupation']

# Just before your print() call, use the del keyword to delete the age key and its value from copper.

del copper['age']

# Step 10

# Now that you got the basic aspects of dictionaries, you can proceed to build the shortest path algorithm.
# Delete every line of code after the declaration of the copper dictionary.

# Step 11

# Graphs are data structures representing relations between pairs of elements. 
# These elements, called nodes, can be real-life objects, entities, points in space or others. 
# The connections between the nodes are called the edges.

# For example, a graph can be used to represent two points in the space, A and B, connected by a path. 
# A graph like this will be made of two nodes connected by an edge.

# Rename the copper dictionary into my_graph. This will represent the graph to test your algorithm.

# Step 12

# Now, replace the existent keys with the strings A and B — one for each node. 
# Then, replace each value with the string representing the node connected to the key.

my_graph = {
    'A': 'B',
    'B': 'A'
}

# Step 13

# Add another node connected to B to your graph and call it C.

# Modify your existing dictionary to represent this arrangement. 
# Use a list to represent the multiple connections of your B node.

my_graph = {
    'A': 'B',
    'B': ['A', 'C'],
    'C': 'B'
}

# Step 14

# Add one last node, D, which is connected with A and C. 
# Modify your dictionary to represent this structure. 
# Again, use a list to represent multiple connections.

my_graph = {
    'A': ['D', 'B'],
    'B': ['A', 'C'],
    'C': ['D', 'B'],
    'D': ['A', 'C']
}

# Step 15

# A graph is called a weighted graph when its edges are associated with weights, representing a distance, 
# time or other quantitative value.

# In your case, these weights will be the distances between each node, or point in space. 
# To represent a weighted graph you can modify your dictionary, using a list of tuples for each value.

# The first element in the tuple will be the connected node, and the second element will be an integer number 
# indicating the distance.

# Modify my_graph["A"] into a list of tuples, considering the following distances:

    # Edge 	Weight
    # A-B 	3
    # B-C 	4
    # C-D 	7
    # D-A 	1

my_graph = {
    'A': [('B', 3), ('D', 1)],
    'B': [('A', 3), ('C', 4)],
    'C': [('B', 4), ('D', 7)],
    'D': [('A', 1), ('C', 7)]
}

# Step 18

# Now you are going to start developing the algorithm to calculate the shortest path between each node 
# in your new graph.

# Declare an empty function called shortest_path and don't forget the pass keyword.

def shortest_path():
    pass

# Step 19

# The algorithm will start at a specified node. 
# Then it will explore the graph to find the shortest path between the starting node, or source, 
# and all the other nodes.

# For that your function needs two parameters: graph, and start. Add them to your function declaration.

# Step 20

# To keep track of the visited nodes, you need a list of all the nodes in the graph. 
# Once a node is visited, it will be removed from that list.

# Now, replace the pass keyword with a variable named unvisited and assign it an empty list.

def shortest_path(graph, start):
    unvisited = []

# Step 21

# Create a for loop to iterate over your graph, and append each node to the unvisited list.

def shortest_path(graph, start):
    unvisited = []
    for node in graph:
        unvisited.append(node)

# Step 22

# While the algorithm explores the graph, it should keep track of the currently known shortest distance between 
# the starting node and the other nodes.

# Before your for loop, create a new variable named distances and assign it an empty dictionary.

# Step 23

# The distance from the starting node is zero, because the algorithm begins its assessment right from there.
# After appending node to unvisited in your loop, create an if statement that triggers if the node is equal to the starting node. Then assign 0 to that node inside the distances dictionary.

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0

# Step 24

# At the beginning, all the other nodes in the graph are considered to be at infinite distance from the 
# source node, because the distance has not been determined yet.

#Create an else clause and assign an infinite value to the node in the distances dictionary. 
# For that, use the float() function with the string inf as argument to generate a floating point number 
# representing the positive infinity.

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')

# Step 25

# After your for loop, add a print() call and pass in the following string to see the values of 
# the variables you have created: f'Unvisited: {unvisited}\nDistances: {distances}'.

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')

# Step 26

# Now, call your function passing my_graph and 'A' as the arguments.

def shortest_path(graph, start):
    unvisited = []
    distances = {}
    for node in graph:
        unvisited.append(node)
        if node == start:
            distances[node] = 0
        else:
            distances[node] = float('inf')
    print(f'Unvisited: {unvisited}\nDistances: {distances}')
shortest_path(my_graph, 'A')



