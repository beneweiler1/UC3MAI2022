
def bell_eq(costs : list, initial_state, probability_matrices : list, states_list_not_final, states_list_final):
    eq = []
    next_V = min[costs[0] + probability_matrices[0][initial_state][]]
    n = 0
    # since there would be the same number of cost than actions
    while n < len(costs):
        prob_action = []
        columns = 0
        while columns < states_list_not_final:
            rows = 0
            prob_action.append(columns)
            list_given_initial = []
            while rows < states_list_final:
                my_row = {}
                list_given_initial["rows"] = probability_matrices[n][columns][rows])







