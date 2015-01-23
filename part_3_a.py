from __future__ import division
import matplotlib.pyplot as plt
from SIS import *

if __name__ == '__main__':
    """Main Function"""
    N, edges, input_graph = read_input()

    trans_p1 = 0.20; trans_p2=0.01 #transmission probability
    heal_p1 = 0.70; heal_p2 = 0.60 #healing probability
    k1 = 200 #number of vaccines

    #### Question 3 Start ######
    #Policy A
    print("\nImmunizing using Policy A ..")
    s_policy_a = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s_policy_a.immune_policy_A( k1 )
    s_policy_a.calculate_eig()
    s_policy_a.calculate_virus_strength(trans_p1, heal_p1)
    print(s_policy_a)

    #Policy B
    print("\nImmunizing using Policy B ..")
    s_policy_b = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s_policy_b.immune_policy_B( k1 )
    s_policy_b.calculate_eig()
    s_policy_b.calculate_virus_strength(trans_p1, heal_p1)
    print(s_policy_b)

    #Policy C
    print("\nImmunizing using Policy C ..")
    s_policy_c = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s_policy_c.immune_policy_C( k1 )
    s_policy_c.calculate_eig()
    s_policy_c.calculate_virus_strength(trans_p1, heal_p1)
    print(s_policy_c)
 
    #Policy D
    print("\nImmunizing using Policy D ..")
    s_policy_d = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
    s_policy_d.immune_policy_D( k1 )
    s_policy_d.calculate_eig()
    s_policy_d.calculate_virus_strength(trans_p1, heal_p1)
    print(s_policy_d)

    
    #Keeping β and δ fixed, analyze how the value of k affect the graph
    #Starting from k = 200 to k = 300 in the steps of 10. 
    #I am starting the K from 200 because, for k=200, there was epidemic in each policy
    print("")
    print("analyze how the value of k affect the graph ..")
    
    #For policy A
    strenth_a = []
    for k in range(200, 300, 10):
        s_policy_a = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
        s_policy_a.immune_policy_A( k )
        s_policy_a.calculate_eig()
        s_policy_a.calculate_virus_strength(trans_p1, heal_p1)
        strenth_a.append(s_policy_a.virus_strength)
    plot_line_graphs( range(200, 300, 10), strenth_a, "Number of vaccines(K)", "Virus Propagation strength")
    
    #For policy B
    print("Policy B:")
    strenth_b = []
    for k in range(200, 300, 10):
        s_policy_b = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
        s_policy_b.immune_policy_B( k )
        s_policy_b.calculate_eig()
        s_policy_b.calculate_virus_strength(trans_p1, heal_p1)
        strenth_b.append(s_policy_b.virus_strength)
    plot_line_graphs( range(200, 300, 10), strenth_b, "Number of vaccines(K)", "Virus Propagation strength")
    
    #For policy C
    print("Policy C:")
    strenth_c = []
    for k in range(200, 300, 10):
        s_policy_c = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
        s_policy_c.immune_policy_C( k )
        s_policy_c.calculate_eig()
        s_policy_c.calculate_virus_strength(trans_p1, heal_p1)
        strenth_c.append(s_policy_c.virus_strength)
    plot_line_graphs(range(200, 300, 10), strenth_c, "Number of vaccines(K)", "Virus Propagation strength")
    
    #For policy D
    print("Policy D:")
    strenth_d = []
    for k in range(2000, 3600, 500):
        s_policy_d = SIS(N, input_graph, transmision_probability = trans_p1, healing_probability = heal_p1)
        s_policy_d.immune_policy_D( k )
        s_policy_d.calculate_eig()
        s_policy_d.calculate_virus_strength(trans_p1, heal_p1)
        strenth_d.append(s_policy_d.virus_strength)
    plot_line_graphs(range(2000, 3600, 500), strenth_d, "Number of vaccines(K)", "Virus Propagation strength")