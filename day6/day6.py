import os
import re
import math

def solve(numbers, operators):
    numbers = [list(map(int, re.sub(" +"," ",line).strip(" ").split(" "))) for line in numbers]
    operators = re.sub(" +"," ",operators).strip(" ").split(" ")
    result = 0
    for col in range(len(numbers[0])):
        op = operators[col]
        operands = [numbers[row][col] for row in range(len(numbers))]
        colvalue = sum(operands) if op=="+" else math.prod(operands)
        result += colvalue
    return result

def solve2(numbers, operators):
    operator_matches = re.finditer(r"([*+] +)",operators)
    result = 0
    for match in operator_matches:
        idx1, idx2 = match.span()
        op = match.group()[0]
        operands = []
        for col in range(idx1,idx2):
            number = "".join(numbers[row][col] for row in range(len(numbers))).strip()
            if number: operands.append(int(number))
        result += sum(operands) if op == "+" else math.prod(operands)
    return result

def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = [line.strip("\n") for line in lines]

    #
    numbers = lines[:-1]
    operators = lines[-1]

    result = solve(numbers,operators)
    print(f"The result 1 is {result}.")

    result = solve2(numbers, operators)
    print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
