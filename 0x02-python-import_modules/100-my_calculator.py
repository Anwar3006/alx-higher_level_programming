#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as cal
    from sys import argv

    Quant = len(argv) - 1
    if Quant != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
   
    # for i in range(Quant):
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, cal.add(a, b)))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, cal.sub(a, b)))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, cal.mul(a, b)))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, cal.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
