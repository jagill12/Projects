from collections import defaultdict
import random

class DeBruijnGraph():
    """Main class for De Bruijn graphs"""

    def __init__(self, input_string, k):
        self.graph = defaultdict(list)
        self.first_node = ''
        self.build_debruijn_graph(input_string, k)
        
    def add_edge(self, left, right):
        """Add an edge from 'left' to 'right' in the graph."""
        self.graph[left].append(right)
        
    def remove_edge(self, left, right):
        """Remove an edge from 'left' to 'right' in the graph."""
        self.graph[left].remove(right)
        
    def build_debruijn_graph(self, input_string, k):
        """Build the De Bruijn graph from the input string and k-mer length."""
        for i in range(len(input_string) - k + 1):
            node = input_string[i:i + k - 1]
            next_node = input_string[i + 1:i + k]
            self.add_edge(node, next_node)
            
            if i == 0:
                self.first_node = node
        
    def eulerian_walk(self, node):
        """Recursive function to find an Eulerian path with randomness."""
        tour = []
        
        while self.graph[node]:
            # Randomly select the next edge
            next_node = random.choice(self.graph[node])
            self.remove_edge(node, next_node)
            tour.extend(self.eulerian_walk(next_node))
        
        tour.append(node)
        return tour

    def print_eulerian_walk(self):
        """Initiate the Eulerian walk starting from the first node."""
        if not self.first_node:
            print("Graph is empty or not properly initialized.")
            return []
        
        tour = self.eulerian_walk(self.first_node)
        tour.reverse() 
        print(tour)
        return tour

dbg = DeBruijnGraph("fool me once shame on shame on you fool me", 6)
walk = dbg.print_eulerian_walk()
reconstructed_string = walk[0] + ''.join(map(lambda x: x[-1], walk[1:]))
print(reconstructed_string)
