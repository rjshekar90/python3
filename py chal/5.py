

class InputOutputStr:

    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input(">>> ")

    def print_string(self):
        return self.s.upper()

x = InputOutputStr()
x.get_string()
print(x.print_string())
