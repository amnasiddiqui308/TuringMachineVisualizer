class Graph:
    def __init__(self, nodes):
        self. nodes = nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v, weight):
        # directed graph
        self.adj_list[u].append((v, weight))

    def print_list(self):
        for node in self.nodes:
            print(node, "->", self.adj_list[node])

    def get_graph_list(self):
        return self.adj_list

    def dijkstra(graph, source):
        visited_nodes = []
        distance_previous = []

        # initialization step
        step = 0
        visited_nodes.append(source)
        nodes = list(graph.get_graph_list().keys())
        source_edges = graph.get_graph_list()[source]
        flag = False
        
        for node in nodes:
            for i in source_edges:
                if i[0] == node and node not in visited_nodes:
                    distance_previous.append([source, i[0], i[1]])
                    flag = True
                    break

            if not flag and node != source:
                distance_previous.append([source, node, float('inf')])
            
            flag = False

        s1 = "step"
        s2 = "N'"
        print(s1.ljust(7, " "), end = " ")
        print(s2.ljust(13, " "), end = " ")

        for edges in distance_previous:
            s3 = "D(" + str(edges[1]) + "), " + "p(" + str(edges[1]) + ")"
            print(s3.ljust(19, " "), end = " ")

        print()
        s2 = ""
        for visited in visited_nodes:
            s2 += str(visited)

        print(str(step).ljust(7, " "), s2.ljust(13, " "), end = " ")

        for edges in distance_previous:
            s3 = str(edges[2]) + ", " + str(edges[0])
            print(s3.ljust(19, " "), end = " ")

        print()

        while len(visited_nodes) != len(nodes):
            step += 1
            min_cost = float('inf')
            for edge in distance_previous:
                if edge[2] < min_cost and edge[1] not in visited_nodes:
                    min_cost_node = edge[1]
                    min_cost = edge[2]

            visited_nodes.append(min_cost_node)
            new_source_edges = graph.get_graph_list()[min_cost_node]

            for node in nodes:
                for i in new_source_edges:
                    if i[0] == node and node not in visited_nodes:
                        for j in distance_previous:
                            if node in j:
                                cost1 = j[2]
                                cost2 = min_cost + i[1]
                                if cost2 < cost1:
                                    j[0] = min_cost_node; j[2] = cost2

            s2 = ""
            for visited in visited_nodes:
                s2 += str(visited)

            print(str(step).ljust(7, " "), s2.ljust(13, " "), end = " ")

            for edges in distance_previous:
                s3 = str(edges[2]) + ", " + str(edges[0])
                print(s3.ljust(19, " "), end = " ")

            print()


edges = [
    ("S", "A", 10), ("S", "C", 5), ("A", "B", 1), ("A", "C", 2), ("B", "D", 4), ("C", "A", 3), ("C", "B", 9), ("C", "D", 2), ("D", "S", 7), ("D", "B", 6)
]
nodes = ['S', 'A', 'B', 'C', 'D']     
graph = Graph(nodes)

for u, v, x in edges:
    graph.add_edge(u, v, x)

print("Graph:")
graph.print_list()
source = 'S'
print("\nDIJKSTRA ALGORITHM (Source Node: " + source + ")")
graph.dijkstra(source = source)
