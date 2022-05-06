from unittest import TestCase
from All.states_creation import States
from All.probability_matix_creator import CalcMatrix
from All.prepare_data import extract

from pathlib import Path
path = str(Path.home()) + "\\Desktop\\uni\\segundo\\ia\\final_AI\\data\\Data.csv"
my_init_state = ["High", "High", "Low"]
names_sem = ["N", "E", "W"]
possible_states = [["High", "High", "High"], ["High", "High", "Low"], ["High", "Low", "High"], ["High", "Low", "Low"],
                   ["Low", "High", "High"], ["Low", "High", "Low"], ["Low", "Low", "High"]]
possible_states_final = [["High", "High", "High"], ["High", "High", "Low"], ["High", "Low", "High"],
                         ["High", "Low", "Low"], ["Low", "High", "High"], ["Low", "High", "Low"],
                         ["Low", "Low", "High"], ["Low", "Low", "Low"]]

existing_states = []
for i in possible_states:
    existing_states.append(States(i))


class TestGetProbabilities(TestCase):
    """Class for testing the obtained probabilities"""
    def setUp(self) -> None:
        """setUp IS EXECUTED ONCE BEFORE EACH TEST"""
        #self.my_function = main_function(path, my_init_state, names_sem)
        self.my_path = path

    # def test_valid_case(self):
    #     """this test checks if main function returns the correct data types"""
    #     my_probabilities_action, my_probabilities_no_action = self.my_function
    #
    #     print(my_probabilities_no_action)
    #     print(my_probabilities_action)
    #     self.assertEqual(my_probabilities_no_action, [0.0, 0.661186848436247, 0.0])

    def test_valid_case_matrix_E(self):
        """this test checks if main function returns the correct data types"""
        my_data = extract(self.my_path, len(names_sem))
        my_matrix = CalcMatrix(my_data, possible_states, possible_states_final,  names_sem).create_matrix("E")
        print(" matrix action E ")
        for row in my_matrix:
            print(row)

    def test_valid_case_matrix_N(self):
        """this test checks if main function returns the correct data types"""
        my_data = extract(self.my_path, len(names_sem))
        my_matrix = CalcMatrix(my_data, possible_states, possible_states_final,  names_sem).create_matrix("N")
        print(" matrix action N")
        for row in my_matrix:
            print(row)

    def test_valid_case_matrix_W(self):
        """this test checks if main function returns the correct data types"""
        my_data = extract(self.my_path, len(names_sem))
        my_matrix = CalcMatrix(my_data, possible_states, possible_states_final,  names_sem).create_matrix("W")
        print(" matrix action W")
        for row in my_matrix:
            print(row)

    def test_valid_case_extract_data(self):
        """this test checks if main function returns the correct data types"""
        my_data = extract(self.my_path, len(names_sem))
        print(my_data)







