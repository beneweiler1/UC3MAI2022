from python.Exceptions_class import MyException

class States:

    def __init__(self, in_list: list):
        # input must be a list with the initial states in order
        self.directions = self.validate_directions(in_list)
        self.len = len(in_list)

    def validate_directions(self, value: list):
        for e in value:
            if e != "High" and e != "Low":
                raise MyException("the input value should be Low or High")
        return value

    def number_directions(self):
        return len(self.in_list)




