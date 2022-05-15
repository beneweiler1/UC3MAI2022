
class Bellman:
    def __init__(self, costs: dict, initial_state, probability_matrices: dict, states_list_not_final,
                 states_list_final, actions):
        self.probability_matrices = probability_matrices
        self.states_list_no_fin = states_list_not_final
        self.states_list_fin = states_list_final



    def bellman_eq(self, v_actual, my_state, action):
        v_new ={}
        v_new[my_state] =
        i = 1
        important_states = []
        for i in range(1,len(self.probability_matrices[action])):
            if self.probability_matrices[action][0] == my_state:
                for state in range (1,len(self.states_final)):
                    if state == 8:
                        my_final_state = state
                    elif self.probability_matrices[action][0][state]> 0.0:
                        important_states.append(state)
                        # state is a number, not a list

        return v_new

    def for_each_state_in_action(self):
        v0 = {}
        for state in self.states_list_no_fin:
            v0[state] = 0
            for i in range (300000000):
                my_new_v = self.bellman_eq(v0, state)
                v0[state] = my_new_v

#
# def bell_eq(costs: dict, initial_state, probability_matrices: dict, states_list_not_final, states_list_final, actions):
#     eq = []
#     next_V = min[costs[0] + probability_matrices[0][initial_state][]]
#
#     # since there would be the same number of cost than actions
#     for action in actions:
#         for state in states_list_final:
#             for i in range(len(probability_matrices[action])):
#                 probability_matrices[action][i]






