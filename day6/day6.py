import os
import re

def solve(numbers, operators):
    result = 0
    numbers = [list(map(int, line.split(" "))) for line in numbers]
    for col in range(len(numbers[0])):
        op = operators[col]
        if op=="+":
            colvalue = 0
        elif op == "*":
            colvalue = 1
        for row in range(len(numbers)):
            if op=="+":
                colvalue += numbers[row][col]
            elif op == "*":
                colvalue *= numbers[row][col]
        result += colvalue

    return result


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    #
    lines = [re.sub(" +"," ",line).strip(" ") for line in lines]
    numbers = lines[:-1]
    operators = lines[-1].split(" ")

    result = solve(numbers,operators)
    print(f"The result 1 is {result}.")
    #result = solve2(lines)
    #print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
