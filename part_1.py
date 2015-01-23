from __future__ import division
import networkx as nx
import matplotlib.pyplot as plt
from SIS import *

if __name__ == '__main__':
    """Main Function"""
    N, edges, input_graph = read_input()

    trans_p1 = 0.20; trans_p2=0.01 #transmission probability
    heal_p1 = 0.70; heal_p2 = 0.60 #healing probability
    k1 = 200 #number of vaccines
    
    sis_1 = SIS(N, input_graph)
    sis_1.calculate_eig()

    sis_1.calculate_virus_strength(trans_p1, heal_p1)
    print(sis_1)
    
    sis_1.calculate_virus_strength(trans_p2, heal_p2)
    print(sis_1)

    #Keeping healing probability fixed and changing transmission prob
    x = []
    y = []
    
    #For heal_p1
    min_trans_prob = 1.0
    for i in np.arange(0.00, 1.00, 0.01):
        sis_1.calculate_virus_strength(i, heal_p1)
        x.append(i)
        y.append(sis_1.virus_strength)
        
        if sis_1.virus_strength > 1 and i < min_trans_prob:
            min_trans_prob = i
    print("Minimum transmission prob for step of 0.05 and heal_prob of " + str(heal_p1) +": " + str(min_trans_prob))       
    plot_line_graphs(x, y, "Transmission prob", "Virus strength")
  
    #For heal_p2
    x.clear()
    y.clear()
    min_trans_prob = 1.0
    for i in np.arange(0.00, 1.00, 0.01):
        sis_1.calculate_virus_strength(i, heal_p2)
        x.append(i)
        y.append(sis_1.virus_strength)
        
        if sis_1.virus_strength > 1 and i < min_trans_prob:
            min_trans_prob = i
    
    print("Minimum transmission prob for step of 0.05 and heal_prob of " + str(heal_p2) +": " + str(min_trans_prob))       
    plot_line_graphs(x, y, "transmision prob", "virus strength")

    #Keeping transmission prob fixed and changing healing probability
    #For trans_p1
    x.clear()
    y.clear()   
    max_heal_prob = 0
    for i in np.arange(0.01, 1.00, 0.05):
        sis_1.calculate_virus_strength(trans_p1, i)
        x.append(i)
        y.append(sis_1.virus_strength)
        
        if sis_1.virus_strength > 1 and i>max_heal_prob:
            max_heal_prob = i         
    print("Maximum transmission prob for step of 0.05 and trans_p of " + str(trans_p1) +": " + str(max_heal_prob))         
    plot_line_graphs(x, y, "healing prob", "virus strength")
    
    #for trans_p2
    x.clear()
    y.clear()
    max_heal_prob = 0
    for i in np.arange(0.01, 1.00, 0.01):
        sis_1.calculate_virus_strength(trans_p2, i)
        x.append(i)
        y.append(sis_1.virus_strength)
        
        if sis_1.virus_strength > 1 and i>max_heal_prob:
            max_heal_prob = i
    print("Maximum transmission prob for step of 0.05 and trans_p of " + str(trans_p2) +": " + str(max_heal_prob))         
    plot_line_graphs(x, y, "healing prob", "virus strength")