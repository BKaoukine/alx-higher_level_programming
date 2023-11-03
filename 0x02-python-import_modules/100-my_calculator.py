#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, sub, mul, add
    from sys import argv, exit

    n_arg = len(argv)
    num_usage = "Usage: ./100-my_calculator.py <a> <operator> <b>"

    if n_arg != 4:
        print("{:s}".format(num_usage))
        exit(1)

    operator = argv[n_arg - 2]
    a = int(argv[1])
    b = int(argv[n_arg - 1])
    valid_operators = ["+", "-", "*", "/"]
    oper_usage = "Unknown operator. Available operators: +, -, * and /"

    if operator not in valid_operators:
        print("{:s}".format(oper_usage))
        exit(1)

    else:
        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
