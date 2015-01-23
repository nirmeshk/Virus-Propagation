from __future__ import division
import matplotlib.pyplot as plt
from SIS import *

if __name__ == '__main__':
    """Main Function"""
    N, edges, input_graph = read_input()

    trans_p1 = 0.20; trans_p2=0.01 #transmission probability
    heal_p1 = 0.70; heal_p2 = 0.60 #healing probability
    k1 = 200 #number of vaccines

    #### Question 3 part F : Simulation of VPM ######
    #Initializing 4 objects. We will use each for different policies
    s_policy_a = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s_policy_b = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s_policy_c = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s_policy_d = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)

    #Immunize the networks with different immunization policies
    s_policy_a.immune_policy_A(k1)
    s_policy_b.immune_policy_B(k1)
    s_policy_c.immune_policy_C(k1)
    s_policy_d.immune_policy_D(k1)

    #Initialize a Numpy matrix with all zeros
    final_matrix_s_a = np.zeros(shape=(100,10))
    final_matrix_s_b = np.zeros(shape=(100,10))
    final_matrix_s_c = np.zeros(shape=(100,10))
    final_matrix_s_d = np.zeros(shape=(100,10))

    # Calculate fraction of infected nodes for each object with different immunization policies
    final_matrix_s_a[0,0] = s_policy_a.c / s_policy_a.N
    final_matrix_s_b[0,0] = s_policy_b.c / s_policy_b.N
    final_matrix_s_c[0,0] = s_policy_c.c / s_policy_c.N
    final_matrix_s_d[0,0] = s_policy_d.c / s_policy_d.N

    for simulation in range(1, 10):
        #Infect the initial nodes
        s_policy_a.infect_initial(); s_policy_b.infect_initial();
        s_policy_c.infect_initial(); s_policy_d.infect_initial();
        for t in range(1, 100):
            #Find susceptible nodes for all 4 networks
            s_policy_a.get_susceptible(); s_policy_b.get_susceptible()
            s_policy_c.get_susceptible(); s_policy_d.get_susceptible()

            #Heal
            s_policy_a.heal(); s_policy_b.heal()
            s_policy_c.heal(); s_policy_d.heal()

            #Infect some nodes out of susceptible
            s_policy_a.infect(); s_policy_b.infect()
            s_policy_c.infect(); s_policy_d.infect()

            #Get Fraction of infected nodes
            final_matrix_s_a[t, simulation] =  s_policy_a.get_fraction_of_infected_nodes()  
            final_matrix_s_b[t, simulation] =  s_policy_b.get_fraction_of_infected_nodes()  
            final_matrix_s_c[t, simulation] =  s_policy_c.get_fraction_of_infected_nodes()  
            final_matrix_s_d[t, simulation] =  s_policy_d.get_fraction_of_infected_nodes()   

    x = range(0,100)

    #calculating sum of each row, and dividing by 10 to find average.
    y_s_a = [ a/10 for a in final_matrix_s_a.sum(axis=1) ] 
    y_s_b = [ a/10 for a in final_matrix_s_b.sum(axis=1) ]
    y_s_c = [ a/10 for a in final_matrix_s_c.sum(axis=1) ]
    y_s_d = [ a/10 for a in final_matrix_s_d.sum(axis=1) ]

    #Plotting both the results.
    plot_line_graphs(x, y_s_a, "time stamp", "average of fraction of infected nodes")
    plot_line_graphs(x, y_s_b, "time stamp", "average of fraction of infected nodes")
    plot_line_graphs(x, y_s_c, "time stamp", "average of fraction of infected nodes")
    plot_line_graphs(x, y_s_d, "time stamp", "average of fraction of infected nodes")