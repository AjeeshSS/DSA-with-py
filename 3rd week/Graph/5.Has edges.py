# to check which are the vertexes are connected using edges
class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        # check if both vertex exist or not.
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            # here we are connecting bidirectional
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def hasEdges(self, v1, v2):
        return v2 in self.adj_list[v1] and v1 in self.adj_list[v2]


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')

my_graph.add_edge('A', 'B') # when calls this ,it forms edges which points bidirectional.

my_graph.print_graph()
print(my_graph.hasEdges('A', 'B'))
print(my_graph.hasEdges('B', 'A'))
