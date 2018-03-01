#!/usr/bin/python3
# NAZAR SHANDRA

import sys

def add(operand1, operand2):
    try:
        return str(operand1 + operand2)
    except TypeError:
        return("add: Type error.")


def sub(operand1, operand2):
    try:
        return str(operand1 - operand2)
    except TypeError:
        return("sub: Type error.")


def mul(operand1, operand2):
    try:
        return str(operand1 * operand2)
    except TypeError:
        return("mul: Type error.")


def div(operand1, operand2):
    try:
        return str(operand1 / operand2)
    except TypeError:
        return("div: Type error.")
    except ZeroDivisionError:
        return("Division by zero error.")


functions = {"add": add, "sub": sub, "mul": mul, "div": div}

operators = {"add": "+", "sub": "-", "mul": "*", "div": "/"}

def to_float(input):
    try:
        return float(input)
    except ValueError:
        return (input + ": Value error.")


def calculator(function, operand1, operand2):

    foperand1, foperand2 = to_float(operand1), to_float(operand2)

    if function in functions:
        result = functions[function](foperand1, foperand2)
        return(operand1 + operators[function] + operand2 + "=" + result)
    else:
        return("wrong function. Usage: add, sub, mul, div.")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit("Usage: calculadora.py function operand1 operand2")


    function = sys.argv[1]
    operand1, operand2 = to_float(sys.argv[2]), to_float(sys.argv[3])

    if function in functions:
        result = functions[function](operand1, operand2)
    else:
        sys.exit("wrong function. Usage: add, sub, mul, div.")

    print(operand1, operators[function], operand2, '=', result)