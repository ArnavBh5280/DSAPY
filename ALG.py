# ADJACENCY LIST IMPLEMENTATION OF GRAPH

# 1. Write a class Graph to implement list representation of a graph data structure.
# 2. In class Graph, define _init() method to initialise instance object variables vertex_count and a dict adj list where key is vertex number and value is a list of adjacent vertices.
# 3. In class Graph, define add_edge() method to add an edge in the graph with given vertices and weight.
# 4. In class Graph, define remove_edge() method to remove an edge from the graph.
# 5. In class Graph, define has_edge() method to check whether an edge exists or not for a given pair of vertices.
# 6. In class Graph, define print_adj_list() method to print adjacency lists of graph

class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={v:[]for v in range(vno)}
    
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v,weight))
            self.adj_list[v].append((u,weight))
        else:
            print("Invalid")
    
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u]=[(vertex,weight)for vertex,weight in self.adj_list[u]if vertex!=v]
            self.adj_list[v]=[(vertex,weight)for vertex,weight in self.adj_list[v]if vertex!=u]
        else:
            print("IInvalid vertices")   
    
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertex==v for vertex, x in self.adj_list[u])
        else:
            print("IInvalid vertices")   
            
    def print_adj_list(self):
        for vertex, n in self.adj_list.items():
            print("V",vertex,":",n)
            
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.print_adj_list()
