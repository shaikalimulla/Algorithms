import math 
import numpy.random as np

'''
Displays the updated scores of AI and User for each round

Input: AI Score, Action by AI, User Score, User input and Matrix
Output: Updated scores of AI and User
'''
def update_scores(M, usr_scr, user_input, ai_scr, action_by_ai):
    old_usr_scr = usr_scr
    usr_scr = (old_usr_scr)+(M[user_input][action_by_ai])
    print ('Old user score: [', old_usr_scr, '], Updated user score: [', usr_scr, '], Difference: [', (usr_scr - old_usr_scr), ']')

    old_ai_scr = ai_scr
    ai_scr = (old_ai_scr)-(M[user_input][action_by_ai])
    print ('Old AI score: [', old_ai_scr, '], Updated AI score: [', ai_scr, '], Difference: [', (ai_scr - old_ai_scr), ']')
          
    return ai_scr, usr_scr

'''
Function to implement the Hedge algorithm in action setting for the AI game.

Input: eta, Matrix and number of rounds
'''
def hedge_algo(eta, M, num_rounds):
    #Initialize all the scores to 0 and weights to 1.
    usr_scr = 0
    ai_scr = 0
    i = 0
    Wts = [1]*len(M[0])
    
    while (i != num_rounds):
        print ('***************************************')
        print (' Round: [', i, ']')
        print ('***************************************')
        
        chk = True
        while (chk):
            user_input = int(input('Enter the row you would like to select:'))
            print ('Action selected by user: [', user_input, ']')
    
            if (user_input < 0 or user_input > 3):
                print ('Incorrect entry!!! Please select the row from 0 to 3')
            else:
                chk = False

        arr = []
        for j in range(len(Wts)):
            arr.append(j)
        prob_distr = []
        for wt in Wts:
            prob_distr.append(wt/sum(Wts))
        action_by_ai = np.choice(arr, p=prob_distr)
        print ('Probability distribution:', prob_distr)
        print ('Action chosen by AI: [', action_by_ai, ']')
        
        loss_vector = M[user_input]
        print ('Loss vector of AI:', loss_vector)

        for j in range(len(Wts)):
            loss = -(eta)*(loss_vector[j])
            Wts[j] = (Wts[j])*(math.exp(loss))
        print ('Weight vector of AI:', Wts)

        ai_scr, usr_scr = update_scores(M, usr_scr, user_input, ai_scr, action_by_ai)
        
        i = i+1;

'''
Main function to run hedge algorithm for AI game
'''
if __name__ == '__main__':
    '''
    Use random_integers in numpy package to generate payoff random matrix
    '''
    M = [[np.random_integers(-10,10),np.random_integers(-10,10),np.random_integers(-10,10)],
             [np.random_integers(-10,10),np.random_integers(-10,10),np.random_integers(-10,10)],
             [np.random_integers(-10,10),np.random_integers(-10,10),np.random_integers(-10,10)],
             [np.random_integers(-10,10),np.random_integers(-10,10),np.random_integers(-10,10)]
        ]    

    num_rounds = int(input('Enter number of rounds you would like to select:'))
    print ('Number of rounds selected by user: [', num_rounds, ']')

    eta = (1) / (math.sqrt(num_rounds))
    print ( 'Generated Payoff Matrix:')
    for row in M:
        print ( row)
    '''
    Pass num of rounds, eta and payoff matrix to hedge function
    ''' 
    hedge_algo(eta, M, num_rounds)