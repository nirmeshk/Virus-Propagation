from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
import math

from SIS import *

if __name__ == '__main__':
    """Main Function"""
    N, edges, input_graph = read_input()

    trans_p1 = 0.20; trans_p2=0.01 #transmission probability
    heal_p1 = 0.70; heal_p2 = 0.60 #healing probability
    k1 = 200 #number of vaccines

    
    #For trans_p1 and heal_p1
    s1 = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s2 = SIS(N, input_graph, transmision_probability = trans_p2, healing_probability = heal_p2)
    c = math.ceil(N/10)

    #Initialize a Numpy matrix with all zeros
    final_matrix_s1 = np.zeros(shape=(100,10))
    final_matrix_s2 = np.zeros(shape=(100,10))
    final_matrix_s1[0,0] = final_matrix_s2[0,0] = c/N

    for simulation in range(1, 10):
        s1.infect_initial(c); s2.infect_initial(c)
        for t in range(1, 100):
            s1.get_susceptible(); s2.get_susceptible()
            s1.heal(); s2.heal()
            s1.infect(); s2.infect()
            final_matrix_s1[t, simulation] =  s1.get_fraction_of_infected_nodes()  
            final_matrix_s2[t, simulation] =  s2.get_fraction_of_infected_nodes()   

    #calculating sum of each row, and dividing by 10 to find average.
    y_s1 = [ a/10 for a in final_matrix_s1.sum(axis=1) ] 
    y_s2 = [ a/10 for a in final_matrix_s2.sum(axis=1) ]
    x = range(0,100)

    #Plotting both the results.
    plot_line_graphs(x, y_s1, "time stamp", "average of fraction of infected nodes")
    plot_line_graphs(x, y_s2, "time stamp", "average of fraction of infected nodes")


