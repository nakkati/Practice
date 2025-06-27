"""
graphs are used to represent relationships between things.
G = (V,E), vertices are also nodes. E is edges or connections between nodes. 
Data structures to represent the graphs:
        Adjacency matrix
        Adjacency list
Graph traversal:
        BFS using queues for discovered but not processed - finding paths, connected paths
        DFS using stacks - finding cycles
Topological sort on directed acyclic graph (DAGs) where nodes are represented in a line
where edges go from from left to right

Weighted graphs:

Minimum spanning trees:
    Prims minimum spanning trees
    Kruskal algorithm - minimum spanning tree for sparse graphs
    Union find data structure for Kruskal algorithm?

Shortest paths:
    Dijkstra's algorithm
    All pairs shortest path
    Floyd's algorithm
    Network flow's and bipartite matching

Randomized min-cut
"""

# Undirected, Unweighted graph - used to find shortest distance between nodes and to color the nodes
from collections import defaultdict, deque
class UnweightedUndirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, vertex_1, vertex_2):
        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)

    def bfs(self, starting_vertex):
        visited = set()
        discovered = deque()

        discovered.append(starting_vertex)
        visited.add(starting_vertex)

        while discovered:
            node = discovered.popleft()
            print(node, end= ' ')
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    discovered.append(neighbor)
                    visited.add(neighbor)

g = UnweightedUndirectedGraph() # TODO
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'D')
g.bfs('A')

# DFS implementation

from collections import defaultdict

class UndirectedUnweightedGraph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.processed = {}
        self.discovered = {}
        self.time = 0
        self.entry_time = {}
        self.exit_time = {}
        self.parent = {}
        self.finished = False
    
    def add_edge(self, vertex_1, vertex_2):
        self.graph[vertex_1].append(vertex_2)
        self.graph[vertex_2].append(vertex_1)
    
    def dfs(self, starting_vertex):
        if self.finished:
            return
        self.discovered[starting_vertex] = True
        self.time += 1
        self.entry_time[starting_vertex] = self.time
        self.process_vertex_early(starting_vertex)

        for i in self.graph(starting_vertex):
            if i not in self.discovered:
                self.parent[i] = starting_vertex
                self.process_edge(starting_vertex, i)
                self.dfs(i)
            elif i in self.discovered:
                if i not in self.processed and self.parent(starting_vertex) != i:
                    self.process_edge(starting_vertex, i)
            
            if self.finished:
                return
        
        self.process_vertex_late(starting_vertex)
        self.exit_time[starting_vertex] = self.time
        self.processed[starting_vertex] = True

    def process_vertext_early(self, vertex):
        """ function gets called when the vertext is first visited """
        print("process vertext early: ", vertex)

    def process_edge(self, vertex_1, vertex_2):
        """ function gets called to process an edge """
        print("process edge: ", vertex_1, vertex_2)

    def process_vertex_late(self, vertex):
        """ function gets called when the vertext is first visited """
        print("process vertext late: ", vertex)
