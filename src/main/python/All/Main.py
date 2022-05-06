import csv
from All.Calculator_probabilities import CalcProb
from All.states_creation import States
from auxiliar.compatibility_checker import Compatible


def main_function(path, my_init_state, names_sem):
    ##########################################################################################
    # obtaining data for our probabilities
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
    print(data)
    ###########################################################################################
    # once we have the data in the correct format to work with it, we ask for the probabilities we need

    # we declare the initial state we want to analyze, checking if data is correct
    ###########################################################################################
    init_state = States(my_init_state).directions
    is_compatible = Compatible(data, my_init_state).check_comp()
    print(init_state)
    ############################################################################################

    # once the data introduced is checked, we can produce the needed probabilities

    my_probabilities_no_action, my_probabilities_action = CalcProb(data, init_state, names_sem).calc()

    # now that we have the needed probabilities calculated, we can apply the decision algorithm

    return my_probabilities_action, my_probabilities_no_action


