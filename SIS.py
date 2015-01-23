from __future__ import division
import networkx as nx
import numpy as np
import scipy
import matplotlib.pyplot as plt
import random
import math

class SIS:
    def __init__(self, N, input_graph, transmision_probability = None, healing_probability = None):
        """Initialize all the variables and graph to be used by all operations"""
        self.N = N
        self.input_graph = input_graph.copy()
        self.virus_strength = 0.0
        self.transmision_probability = transmision_probability
        self.healing_probability = healing_probability 
        self.infected = []
        self.susceptible = []
        self.c = 0

    def calculate_eig(self):
        """A function that calculates the eigen value of current adjacency matrix of graph"""
        print("calculating eigen value..")
        self.N = nx.number_of_nodes(self.input_graph)
        eig_value = scipy.sparse.linalg.eigsh(nx.to_numpy_matrix(self.input_graph), 
            k=1, which='LM', return_eigenvectors=False, mode='normal')

        self.max_eig_value = max(eig_value)
        print("Max eig value: " + str(self.max_eig_value))

    def calculate_virus_strength(self, transmision_probability, healing_probability):  
        """ A function to calculate strength of the virus"""
        self.transmision_probability = transmision_probability
        self.healing_probability = healing_probability 
        Cvpm = self.transmision_probability / self.healing_probability
        self.virus_strength = self.max_eig_value * Cvpm
        return self.virus_strength

    def infect_initial(self):
        """ Infect the initial nodes of graph"""
        self.c = math.ceil(self.N/10)
        self.infected.clear()

        #Choose c random nodes from graph to infect. Add them to infected nodes list
        self.infected = random.sample( nx.nodes(self.input_graph) , self.c )

    def get_susceptible(self):
        self.susceptible.clear()
        #Add each neighbor of infected nodes to susceptible list
        for node in self.infected:
            neighbours = self.input_graph.neighbors(node)
            self.susceptible.extend(neighbours)
        #Now remove all the infected nodes from susceptible
        self.susceptible = list( set(self.susceptible).difference(set(self.infected)) )

    def infect(self):
        for node in self.susceptible:
            #Choose a random variable x between [1,0]
            x = random.random() 

            #If x is less that transmision_probability, infect the node
            if x <= self.transmision_probability:
                self.infected.append(node)

    def heal(self):
        for node in self.infected[:]:
            #Choose a random variable x between [1,0]
            x = random.random()
            #If x is less that healing_probability, heal the node, remove it from infected list
            if x <= self.healing_probability:
                self.infected.remove(node)

    def get_fraction_of_infected_nodes(self):
        # Infected length / total nodes
        return len(self.infected) / self.N 

    def immune_policy_A(self, K):
        """Select k random nodes for immunization."""
        nodes = random.sample( range(0,self.N) , K )
        #remove the immunized nodes from graph
        self.input_graph.remove_nodes_from(nodes)
        #reset the number of nodes
        self.N = nx.number_of_nodes(self.input_graph)

    def immune_policy_B(self, K):
        """Select the k nodes with highest degree for immunization."""
        degree = nx.degree(self.input_graph)
        #Sort the nodes depending upon degree
        highest_degree_nodes  = [x for x,y in sorted(degree.items(), key=lambda x: x[1], reverse=True)]
        #remove the immunized nodes from graph
        self.input_graph.remove_nodes_from( highest_degree_nodes[:K] )
        self.N = nx.number_of_nodes(self.input_graph)

    def immune_policy_C(self, K):
        """Select the node with the highest degree for immunization. Remove this node (and its
incident edges) from the contact network. Repeat until all vaccines are administered."""
        for i in range(K):
            degree = nx.degree(self.input_graph)
            max_degree_node = max(degree.items(), key=lambda x: x[1])[0]
            #remove the immunized nodes from graph
            self.input_graph.remove_node( max_degree_node )
        self.N = nx.number_of_nodes(self.input_graph)

    def immune_policy_D(self, K):
        """Find the eigenvector corresponding to the largest eigenvalue of the contact network’s
adjacency matrix. Find the k largest (absolute) values in the eigenvector. Select the k nodes at the
corresponding positions in the eigenvector."""
        print("Calculating Eigen value for Policy D..")
        self.N = nx.number_of_nodes(self.input_graph)
        
        #Calculate highest eigen value and vector
        eig_value, eig_vector = scipy.sparse.linalg.eigsh( nx.to_numpy_matrix(self.input_graph), 
            k=1, which='LM', return_eigenvectors=True, mode='normal')

        #Create a list of tuples (a,b) where a = index and b = absolute value of element in eig_vector
        #And sort this based on absolute value
        eig_vector_list = sorted(
            [(a, abs(b)) for a, b in enumerate(eig_vector)], key = lambda x: x[1], reverse=True)

        #get index of k highest absolute values from Eigen vector
        nodes = [eig_vector_list[i][0] for i in range(K)]
        #remove the immunized nodes from graph
        self.input_graph.remove_nodes_from(nodes)
        self.N = nx.number_of_nodes(self.input_graph)
        
    def __repr__(self):
        """ A function for proper representation """
        return_str = "transmision_probability: " + str(self.transmision_probability)
        return_str += "\nhealing_probability: " + str(self.healing_probability) 
        return_str += "\nvirus strength: " + str(self.virus_strength)
        return return_str

def read_input():
    """ A function to read input file and create networkx graph"""
    print("reading input file..")
    graph_file = open('../data/static.network','r')
    nodes, edges = [int(x) for x in graph_file.readline().split(' ')]
    G = nx.Graph()
    for line in graph_file:
        a, b = [int(x) for x in line.split(' ')]
        G.add_edge(a,b)
    return nodes,edges,G

def plot_line_graphs(x, y, xlab, ylab):
    """ A wrapper function to create line plot"""
    plt.plot( x, y, 'b')
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()