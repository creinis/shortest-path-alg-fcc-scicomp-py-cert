# Shortest Path Algorithm

###### Technologies:
<p align="center">
<img src="https://img.icons8.com/color/75/000000/python.png" width="75" height="75" alt="Python" style="margin: 10px 15px 0 15px;" />
</p>

### Try it!

To run the Shortest Path Algorithm application, follow the instructions in the Setup section below.

## Project Structure

- `shortest_path.py`: Contains the implementation of the Shortest Path Algorithm function.

## Setup

### Prerequisites

- Python 3 installed

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/creinis/shortest-path-alg-fcc-scicomp-py-cert.git
   cd shortest-path-alg-fcc-scicomp-py-cert
   ```

2. Run the Shortest Path Algorithm script:
   ```bash
   python3 shortest_path.py
   ```

## Shortest Path Algorithm

### Functionality

The Shortest Path Algorithm finds the shortest path and its distance between nodes in a weighted graph. It uses Dijkstra's algorithm to calculate the shortest path from a starting node to all other nodes in the graph and prints the paths and distances to the console.

### Practical Use Case

The Shortest Path Algorithm is useful in various applications such as route planning, network optimization, and geographical mapping. It helps in determining the most efficient path between points, which can be applied in transportation systems, logistics, and communication networks.

### Benefits

- **Efficiency:** Computes the shortest path efficiently using Dijkstra's algorithm.
- **Versatility:** Can be used with any weighted graph to find shortest paths.
- **Clear Output:** Provides a clear output of distances and paths from the start node to all other nodes.
- **Python Standard Library:** Utilizes Python’s built-in data structures for implementation.

## How to Use

1. Run the `shortest_path.py` script:
   ```bash
   python3 shortest_path.py
   ```

2. Call the `shortest_path` function with the graph, start node, and optionally a target node.

### Example Usage

```python
from shortest_path import shortest_path

# Define the graph
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

# Calculate shortest paths from node 'A'
distances, paths = shortest_path(my_graph, 'A')

# Print shortest paths and distances
print(distances)
print(paths)
```

### Example Output

```plaintext
A-B distance: 5
Path: A -> B

A-C distance: 3
Path: A -> C

A-D distance: 4
Path: A -> C -> D

A-E distance: 8
Path: A -> C -> E

A-F distance: 7
Path: A -> B -> F
```

## Function Parameters

- `graph`: A dictionary where keys are node labels and values are lists of tuples representing neighboring nodes and edge weights.
- `start`: The starting node for the shortest path calculation.
- `target`: An optional target node to print the shortest path and distance to a specific node (default is an empty string, which means all nodes).

### Constraints

- The graph should be a weighted graph represented as an adjacency list.
- Node labels should be strings and edges should have non-negative weights.

---
#### This is a FreeCodeCamp Challenge for Scientific Computing with Python Projects Certification.
<p align="center">
<img src="https://cdn.freecodecamp.org/platform/universal/fcc_primary.svg" width="250" height="75" alt="freeCodeCamp" style="margin: 0 15px; opacity: 0.6" />
</p>
