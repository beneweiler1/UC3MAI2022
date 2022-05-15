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
my_optimal_policy = main_function(random.randrange(0, 3), 1.5)
print(my_optimal_policy)



def simulator(state, goal, counter=0, my_optimal_policy_ = None):

    # for element in comboBinary:
    if counter == 0:
        my_optimal_policy_ = main_function(random.randrange(0, 3), 1)
    if state == goal:
         # print(state)
        print("we made it")
        return "the number of steps needed where" + str(counter)

    else:
        my_state_array = np.array(state)
        policy_for_my_state = my_optimal_policy_[str(my_state_array)]
        # print(policy_for_my_state)
        arrN, arrW, arrE = array_maker()
        index_state = comboBinary.index(state)
        #index_state = np.where(comboBinary == state)[0][0]
        previous_probability = 0
        my_ranges = []
        # we create the ranges for the probabilities for each state
        if policy_for_my_state == "N":
            for n_state in range(1, len(comboBinary) + 1):
                probability = arrN[index_state + 1][n_state]
                total_range = probability + previous_probability
                my_ranges.append(total_range)
                previous_probability = total_range
        elif policy_for_my_state == "W":
            for n_state in range(1, len(comboBinary) + 1):
                probability = arrW[index_state + 1][n_state]
                total_range = probability + previous_probability
                my_ranges.append(total_range)
                previous_probability = total_range
        elif policy_for_my_state == "E":
            for n_state in range(1, len(comboBinary) + 1):
                probability = arrE[index_state + 1][n_state]
                total_range = probability + previous_probability
                my_ranges.append(total_range)
                previous_probability = total_range
        my_random_number = random.uniform(0, 1)
        for my_range in my_ranges:
            if my_random_number < my_range:
                index_ = my_ranges.index(my_range)
                # print("new state is" + str(comboBinary[index_]))
                simulator(comboBinary[index_], goal, counter + 1, my_optimal_policy_)


steps = simulator([1, 1, 1], [0, 0, 0])
print( steps )





