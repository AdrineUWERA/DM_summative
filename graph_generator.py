"""
A PROGRAM TO GENERATE A RANDOM GRAPH, CHECK IF THE GENERATED GRAPH IS CONNECTED, THEN CHECK IF THE GRAPH HAS
AN EULER PATH OR AND EULER CIRCUIT. AND WHEN THE GRAPH HAS A EULER CIRCUIT THEN THE PROGRAM WILL OUTPUT THE EULER
CIRCUIT
"""

# Importing libraries needed for the program
from collections import defaultdict     # imports defaultdict from collections library
from itertools import combinations      # imports combinations from itertools library
from random import random               # imports random from random library
import networkx                         # imports network library
from matplotlib import pyplot           # imports plylot form matplotlib library
from copy import copy


# a class for graph
class Graph:
    # constructor to initialize the graph properties
    def __init__(self, vertices):
        # a variable to store the vertices of the graph
        self.vertices = vertices

        # default dictionary to store vertices and their neighbors
        # the graph is represented as adjacent list
        self.graph = defaultdict(list)

    # a method to check if the graph has an euler path or an euler circuit
    def check_euler_connection(self):
        # a variable to keep track of the number of vertices with odd degree present in the graph
        odd_degree_vertices = 0

        # loops through the list of vertices
        for vertex in self.vertices:
            # check if the degree of the vertex is odd
            if len(self.graph[vertex]) % 2 != 0:
                odd_degree_vertices += 1

        # check if the total number of odd degree vertices is equal to 0
        if odd_degree_vertices == 0:
            self.get_euler_connection()
            # if the odd degree vertices is equal to 0 then the graph has an euler circuit
            return "The graph has an Euler circuit"

        # check if the total number of odd degree vertices is equal to 2
        elif odd_degree_vertices == 2:
            self.get_euler_connection()
            # if the odd degree vertices is equal to 2 then the graph has an euler path
            return "The graph has an Euler Path"
        else:
            # displayed if a graph does not have an euler path and euler circuit
            return "The graph has neither the Euler path nor Euler path"

    # a method that checks the degrees of a connected graph. The number vertices in the list determines whether has a
    # eularian circuit , path or neither. used by get_euler_connection().
    def check_odd_vertices(self):
        odd_degree_vertices_list = []
        for i in self.graph:  # checking each node in the graph
            if len(self.graph[i]) % 2 != 0:  # Checking if number of connected nodes to a root node are even or odd
                odd_degree_vertices_list.append(i)  # if a node has odd degree than append it to the list
        return odd_degree_vertices_list  # return odd degree nodes list

    # a method that creates a list of the edges in the generated graph. used by get_euler_connection()
    def graph_edges(self):
        edges = []  # empty links list
        for vertex in self.graph:  # for every node in graph
            for neighbour in self.graph[vertex]:  # connected nodes
                edges.append((vertex, neighbour))  # append link to the links list
        return edges  # return links list

    # checks if an edge removed when the program is creating a euler circuit or path is makes the graph disconnected
    # i.e. is a bridge/cut edge. Method is used by get_euler_connection().
    def check_connected_or_not(self, graph):
        vertices = []
        edges = []
        for v in graph:
            vertices.append(v)
            for n in graph[v]:
                edges.append((v, n))

        g = networkx.Graph()
        g.add_nodes_from(vertices)
        g.add_edges_from(edges)
        return networkx.is_connected(g)

    # a method that creates the euler path/circuit for graphs that satisfy the condition
    def get_euler_connection(self):
        u = ""
        v = ""
        bridge = ""
        odd_vertices = self.check_odd_vertices()  # variable for list of odd nodes
        g = copy(self.graph)  # copy our main graph to variable g
        trail = []  # initial trail of the eulerian circuit or path
        if len(odd_vertices) == 2:  # the first node if graph has two odd degree nodes
            u = odd_vertices[0]
        elif len(odd_vertices) == 0:  # the starting node if graph nodes have even degrees
            u = list(g)[0]

        current_vertex = u  # the current vertex or node

        while len(self.graph_edges()) > 0:  # loop runs till no of links becomes zero
            for v in g[current_vertex]:  # first connected node to our starting node
                g[current_vertex].remove(v)  # we go up to the connected node and remove the link from the graph
                g[v].remove(current_vertex)  # do the opposite to remove the current vertex from the connected node
                bridge = not self.check_connected_or_not(g)  # after moving up in our trail we will check if that
                # previous vertex still has links, if not it will be removed from the graph
                if bridge:
                    # if the edge that was just removed by the program was a bridge edge then the program
                    # adds it back to avoid disconnecting the graph
                    g[current_vertex].append(v)
                    g[v].append(current_vertex)
                else:
                    break

            if bridge:
                g[current_vertex].remove(v)
                g[v].remove(current_vertex)
                g.pop(current_vertex)  # popping out node that has no links left
            trail.append((current_vertex, v))  # append the link to our trail list
            current_vertex = v  # updating value of current vertex

        print(f'Eulerian trail: {trail}')  # printing out our trail

    # function to generate graph and check if the graph is connected
    def generate_graph(self):
        # creates a set containing all the vertices
        v = set([i for i in self.vertices])
        # a list to store the edges of the graph
        e = list()
        occurrence = 0.5  # we set p so as to have a normally distributed possibilities

        # Loops through maximum number of edges in a graph (nc2)
        for edge in combinations(v, 2):
            a = random()    # a random probability that the edge will be connected

            # check whether the probability of having an edge is less than the probability
            # that the graph will be connected.
            if a < occurrence:
                # appends the edge to the edge list e
                e.append(edge)

        # loops through the list of edges e
        for edge in e:
            # gets the neighbours of each vertex and append them to the dictionary for the graph
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        print(self.graph)
        # creates an object of the Graph method from networkx library
        random_graph = networkx.Graph()
        # adds all the edges of the graph
        random_graph.add_nodes_from(v)
        # adds all the vertices of the graph
        random_graph.add_edges_from(e)

        # checks if the graph is connected using is_connected function from networkx library
        connected = networkx.is_connected(random_graph)

        # checks if the truth value for if the graph connected is true
        if connected is True:
            # displayed to indicate that the graph is connected
            print("The graph is connected")

            # calls the check_euler_connection() method to check if the graph has an euler connection
            print(self.check_euler_connection())

        else:
            # displayed when the truth value for if the graph is connected is false
            print("The Graph is not connected")

        # a variable to
        position = networkx.spring_layout(random_graph)

        # Then after, we visualise the graph depending on the position of nodes given
        # above.
        networkx.draw_networkx(random_graph, position)

        # The title of the graph and finally showing the graph
        pyplot.title("Random Graph ")
        pyplot.show()


# list of 10 vertices
node = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# creates a graph object and passes in the number of vertices
graph1 = Graph(node)

# calls the generate_graph method
graph1.generate_graph()
