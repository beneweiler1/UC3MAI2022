import csv
from pathlib import Path
from src.main.python.Calculator_probabilities import CalcProb
from src.main.python.states_creation import States
from auxiliar.compatibility_checker import Compatible


def extract(path, num_dir):
    ##########################################################################################
    # obtaining data for our probabilities
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        # create list with first state:
    sem = []
    end_state = []
    init_state = []
    for row in data:
        i = 0
        my_is = []
        my_sem = []
        my_es = []

        while i < (num_dir * 2 + 1):

            if i < num_dir:
                my_is.append(row[i])
            elif i == num_dir:
                my_sem.append(row[i])
            else:
                my_es.append(row[i])
            i += 1
        init_state.append(my_is)
        sem.append(my_sem)
        end_state.append(my_es)

    elem = 0
    my_new_data = []

    while elem < len(init_state):
        new_row = [init_state[elem], sem[elem], end_state[elem]]
        my_new_data.append(new_row)
        elem += 1


    return my_new_data






