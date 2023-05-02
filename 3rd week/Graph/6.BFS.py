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

    """
    The algorithm starts with marking the start vertex as visited and adding it to the queue. Then,
     it dequeues a vertex from the queue, prints it, and marks its adjacent vertices as visited and adds 
     them to the queue. The process continues until the queue is empty.
    """

    def bfs(self, start_vertex):
        visited = {}
        for vertex in self.adj_list:
            visited[vertex] = False

        # Create a list to act as a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)

        while queue:
            # Dequeue a vertex from queue and print it
            current_vertex = queue.pop(0)
            print(current_vertex, end=' ')

            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it
            # visited and enqueue it
            for adjacent_vertex in self.adj_list[current_vertex]:
                if not visited[adjacent_vertex]:
                    visited[adjacent_vertex] = True
                    queue.append(adjacent_vertex)


my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_vertex('D')

my_graph.add_edge('A', 'B')
my_graph.add_edge('A', 'D')
my_graph.add_edge('B', 'C')
my_graph.add_edge('C', 'D')

my_graph.print_graph()
print()
my_graph.bfs('A')
"""Using GPS navigation system BFS is used to find neighboring places.BFS is useful in finding the shortest path in 
an unweighted graph. In this algorithm, we start at the source vertex and explore all its neighbors first, 
then move to their neighbors, and so on, until we reach the destination vertex. BFS is guaranteed to find the 
shortest path if the graph is unweighted. It can also be used to detect if there is a path between two vertices in a 
graph. """
