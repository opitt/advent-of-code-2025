import os
import re

def solve(ranges,matches2):
    numbers = []
    if matches2: regex=r"^(.+)\1{1}"
    else: regex= r"^(.+)\1+"
    for a,b in [list(map(int,range.split("-"))) for range in ranges]:
        for s in [str(n) for n in range(a,b+1)]:
            match = re.fullmatch(regex,s)
            if match:
                numbers.append(int(s)) 

    return sum(numbers)


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines[0].split(","), True)
    print(f"The result 1 is {result}.")
    result = solve(lines[0].split(","), False)
    print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
