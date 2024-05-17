# to check vertexes are connected using edges
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

    def count_edges(self):
        num_edges = 0
        for vertex in self.adj_list:
            num_edges += len(self.adj_list[vertex])
        # Divide by 2 since each edge is counted twice (once for each vertex)
        return num_edges // 2


my_graph = Graph()
my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'D')

my_graph.print_graph()
print('\n no: of edges: ', my_graph.count_edges())
