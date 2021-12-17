"""
A PROGRAM TO CHECK THE NUMBER OF GRAPHS WITH EULER CIRCUIT WITHIN 500 TRIALS.
THE PROGRAM ALSO COUNTS THE NUMBER OF CONNECTED GRAPHS.
THIS PROGRAM WILL HELP TO ESTIMATE THE PROBABILITY OF HAVING A EULER CIRCUIT GIVEN THAT THE GRAPH IS CONNECTED.
"""

# Importing libraries needed for the program
from collections import defaultdict  # imports defaultdict from collections library
from itertools import combinations  # imports combinations from itertools library
from random import random  # imports random from random library
import networkx  # imports network library


# a class for graph
class Graph:
    # constructor to initialize the graph properties
    def __init__(self, vertices):
        # a variable to store the vertices of the graph
        self.vertices = vertices

        # default dictionary to store vertices and their neighbors
        # the graph is represented as adjacent list
        self.graph = defaultdict(list)

    def check_odd_vertices(self):
        odd_degree_vertices_list = []
        for i in self.graph:  # checking each node in the graph
            if len(self.graph[i]) % 2 != 0:  # Checking if number of connected nodes to a root node are even or odd
                odd_degree_vertices_list.append(i)  # if a node has odd degree than append it to the list
        return len(odd_degree_vertices_list)  # return odd degree nodes list

    # function to generate graph and check if the graph is connected
    def generate_graph(self):
        # creates a set containing all the vertices
        v = set([i for i in self.vertices])
        # a list to store the edges of the graph
        e = list()
        occurrence = 0.5  # we set p so as to have a normally distributed possibilities

        # Loops through maximum number of edges in a graph (nc2)
        for edge in combinations(v, 2):
            a = random()  # a random probability that the edge will be connected

            # check whether the probability of having an edge is less than the probability that the graph will be connected.
            if a < occurrence:
                # appends the edge to the edge list e
                e.append(edge)

        # loops through the list of edges e
        for edge in e:
            # gets the neighbours of each vertex and append them to the dictionary for the graph
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        # print(self.graph)
        # creates an object of the Graph method from networkx library
        random_graph = networkx.Graph()
        # adds all the edges of the graph
        random_graph.add_nodes_from(v)
        # adds all the vertices of the graph
        random_graph.add_edges_from(e)

        # checks if the graph is connected using is_connected function from networkx library
        connected = networkx.is_connected(random_graph)

        return connected


# list of 10 vertices
node = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# creates a graph object and passes in the number of vertices
graph1 = Graph(node)


# a function to check the number of connected graphs and euler circuit
def main():
    number_of_trials = 0    # counts the number of trials
    connected_graphs = 0    # counts the number of connected graphs
    euler_circuit = 0       # counts the number of graphs with euler circuits

    # A loop to run the program 500 times to generate graph, check the number of connected graph, and graphs with
    # euler circuit
    while number_of_trials < 500:
        number_of_trials += 1   # increments the number of trials each time a graph is connected

        # checks if the graph is connected
        if graph1.generate_graph() == True:
            connected_graphs += 1   # increments the number of connected graphs

            # checks if the graph has zero number of odd degree vertices, if so, then it's a euler circuit
            if graph1.check_odd_vertices() == 0:
                euler_circuit += 1  # increments the number of graphs with euler circuit
                # break
        else:
            continue
    # displays the number of trials, number of connected graphs and number of graphs of with euler circuit
    print(f"Trials: {number_of_trials}\n"
          f"Connected graphs: {connected_graphs}\n"
          f"Euler circuits from connected graphs: {euler_circuit}\n"
          f"Probability of a Euler circuit given that it is a connected graph: {euler_circuit/connected_graphs:.3f}")


# calls the main function
if __name__ == "__main__":
    main()
