import os
os.system("color 0B")
x = 1
op = 1
def far(x):
    return (float(x) / 5) * 9 + 32
def cel(x):
    return (float(x) - 32) * 5 / 9

def calc(x, op):
    while True:
        print("                             ")
        print("1.Fahrenheit -> Celsius")
        print("2.Fahrenheit <- Celsius")
        op = input("1/2: ")

        if op in ("1", "2"):
            x = input("Starting Temp: ")
            try:
                x = float(x)
                if op == "1":
                    print(x, "converted to Celsius is ", cel(x))
                elif op == "2":
                    print(x, "converted to Fahrenheit is ", far(x))
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")
while True:
    calc(x, op)
