import math 
import random as rand
import numpy as np
import matplotlib.pyplot as py_plot 

'''
Generate a graph with the regret of hedge which shows theta(sqrt(num_rounds))

Input: Regret List, number of rounds
Output: Graph using scatter plot 
'''
def generate_graph(regret_list, num_rounds):
    const1 = 20
    const2 = 2

    const1_num_rounds = []
    for i in num_rounds:
        const1_num_rounds.append(const1*math.sqrt(i))

    const2_num_rounds = []
    for i in num_rounds:
        const2_num_rounds.append(const2*math.sqrt(i))
        
    py_plot.figure()
    plot1 = py_plot.scatter(num_rounds,regret_list,color='black')
    plot2 = py_plot.scatter(num_rounds,const1_num_rounds,color='red')
    plot3 = py_plot.scatter(num_rounds,const2_num_rounds,color='blue')

    py_plot.title("Plot of Regret, bounded by const1*sqrt(num_rounds) and const2*sqrt(num_rounds)")
    py_plot.legend((plot1, plot2, plot3),('Regret', '(const1)*(sqrt(num_rounds))', '(const2)*(sqrt(num_rounds))'), loc=2)

    py_plot.xlabel('Rounds')
    py_plot.ylabel('Regret')
    py_plot.show()

'''
Function to implement the Hedge algorithm in action setting for the AI game.

Input: eta, number of rounds and number of actions
Output: Regret for each round hedge algorithm executed
'''
def hedge_algo(eta, rounds, N):
    action_loss_list = [0]*N
    Wts = [1]*N
    algo_loss = 0
    i = 0
    while (i!=rounds):
        prob_distr = []
        for wt in Wts:
            prob_distr.append(wt/sum(Wts))
            
        loss_vector = []
        temp = 0
        #We are asked to allow nature to decide loss vectors in range [0,1]
        while (temp!=N):
            loss_vector.append(rand.uniform(0.0, 1.0))
            temp = temp+1
        
        temp = 0
        while(temp!=len(action_loss_list)):
            #determine algorithm loss for each time hedge runs
            for l,p in zip(loss_vector, prob_distr):
                algo_loss+= (l*p)
            
            #Update weights
            for j in range(len(Wts)):
                loss = -(eta)*(loss_vector[j])
                Wts[j] = (Wts[j])*(math.exp(loss))
                
            #update loss per action with loss vector    
            action_loss_list[temp]+= loss_vector[temp]

            temp = temp+1
        i = i+1

    return ((algo_loss)-(np.min(action_loss_list)))

'''
Main function to run hedge algorithm to determine regrets and bounds
'''
if __name__ == '__main__':
    num_rounds = []
    regret_list = []
    reg_bound = []

    N = 2    
    rounds =  2
    num_times = 1000
    
    while (rounds!=num_times):
        num_rounds.append(rounds)
        eta = math.sqrt((8*math.log(N))/rounds)
        
        regret = hedge_algo(eta, rounds, N)
        regret_list.append(regret)

        reg_bound.append(math.sqrt((rounds/2)*(math.log(N))))
        
        rounds += 1;
    
    #for r, b in zip(regret_list, reg_bound):
    #    print r, b
    generate_graph(regret_list, num_rounds)
