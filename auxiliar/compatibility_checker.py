from src.main.python.Exceptions_class import MyException
class Compatible:
    def __init__(self, data, init_state):
        self.init_state = init_state
        self.data = data

    def check_comp(self):
        if len(self.init_state) != (len(self.data[0])//2):
            raise MyException("The format is not correct")
        return True

