from calc import Calc


n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
operation = int(input(""">>>Operation<<<
    [1] Sum
    [2] Subtraction
    [3] Division
    [4] Multiplication
"""))

calc = Calc(n1, n2)
print(f"Result: {calc.calculate(operation)}")