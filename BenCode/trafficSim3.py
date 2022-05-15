import random
import pandas as pd
import numpy as np
from BenCode.costDifference import main_function
from BenCode.costDifference import array_maker

# comboBinary = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
comboBinary = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
#print(random.randrange(0, 3))
#print(comboBinary.index([0, 0, 0]))
arrN, arrW, arrE = array_maker()
#print(arrN)
my_optimal_policy = main_function(random.randrange(0, 3), 1)
#print(my_optimal_policy)



def simulator(state, goal, counter=0, my_optimal_policy_ = None):

    # for element in comboBinary:
    if counter == 0:
        my_optimal_policy_ = main_function(0, 1)

    while state != goal:
        # print(state[0])
        counter += 1
        my_state_array = np.array(state[0])
        policy_for_my_state = my_optimal_policy_[str(my_state_array)]
        # print(policy_for_my_state)
        arrN, arrW, arrE = array_maker()
        index_state = comboBinary.index(state[0])
        #index_state = np.where(comboBinary == state)[0][0]
        previous_probability = 0
        my_ranges = []
        # we create the ranges for the probabilities for each state
        if policy_for_my_state == "N":
            array_probabilities = arrN
            # print("N")
        elif policy_for_my_state == "W":
            array_probabilities = arrW
            # print("W")
        elif policy_for_my_state == "E":
            array_probabilities = arrE
            # print("E")
       # print(array_probabilities[index_state+1][1:9])
        state = random.choices(comboBinary, array_probabilities[index_state+1][1:9])

    print("we made it")
    return "the number of steps needed where " + str(counter)



steps = simulator([[1, 1, 1]], [[0, 0, 0]])
print(steps)





