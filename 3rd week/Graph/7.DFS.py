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
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    """The algorithm initializes a dictionary 'visited' to keep track of the visited vertices, and calls the dfs_helper 
    function to perform the actual traversal. The dfs_helper function marks the current vertex as visited, prints it, 
    and then recursively calls itself for each unvisited adjacent vertex. """

    def dfs(self, start_vertex):
        visited = {}
        for vertex in self.adj_list:
            visited[vertex] = False

        self.dfs_helper(start_vertex, visited)

    def dfs_helper(self, current_vertex, visited):
        # Mark the current vertex as visited and print it
        visited[current_vertex] = True
        print(current_vertex, end=' ')

        # Recur for all the adjacent vertices if they haven't been visited
        for adjacent_vertex in self.adj_list[current_vertex]:
            if not visited[adjacent_vertex]:
                self.dfs_helper(adjacent_vertex, visited)


my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'D')yuh

my_graph.print_graph()
print()
my_graph.dfs('A')
"""Depth-first search is used in topological sorting, scheduling problems, cycle detection in graphs, and solving 
puzzles with only one solution, such as a maze or a sudoku puzzle. Other applications involve analyzing networks, 
for example, testing if a graph is bipartite.DFS is useful in detecting cycles in a graph and in exploring all 
possible paths in a graph. In this algorithm, we start at the source vertex and explore as far as possible along each 
branch before backtracking. DFS is useful in topological sorting, finding strongly connected components, and solving 
problems related to trees. """
