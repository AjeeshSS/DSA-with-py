class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():  # check a vertex is already present or not.
            self.adj_list[vertex] = []
            return True
        return False


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.print_graph()
"""
complexity of graph is V+E  (sum of vertex and edges) 
Note that the graph is implemented using adj_list. 
Graphs have various applications in computer science, including: 
Social networks: Graphs can be used to represent social networks where people are nodes and relationships are edges. 

Pathfinding: Graphs can be used to find the shortest path between two points, such as in GPS navigation or in finding 
the most efficient route in logistics. 

Network flow: Graphs can be used to model and optimize flow in transportation systems, telecommunication networks, 
and other systems where resources need to be allocated efficiently. 

Image processing: Graphs can be used to represent images as pixels, where edges represent relationships between 
adjacent pixels. This can be used for tasks such as object recognition or image segmentation. 

Computer networks: Graphs can be used to model and optimize the flow of data in computer networks, such as in routing 
packets through the internet. 
"""
