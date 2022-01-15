from math import pow

class Calc():

    # Cosntructor
    def __init__(self, n1=0, n2=0):
        self.n1 = n1
        self.n2 = n2

        pass

    # Operations
    def sum(self):
        return self.n1 + self.n2

    def sub(self):
        return self.n1 - self.n2
    
    def mult(self):
        return self.n1 * self.n2
    
    def div(self):
        return self.n1 / self.n2

    def pow(self):
        return self.n1**self.n2

    # Calculate
    def calculate(self, op):
        if op == 1:
            return self.sum()

        elif op == 2:
            return self.sub()

        elif op == 3:
            return self.div()

        elif op == 4:
            return self.mult()

        elif op == 5:
            return self.pow()

        else:
            return "Invalid operation option"
