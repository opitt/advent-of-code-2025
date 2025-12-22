import os

def solve(lines, count_zeros_passed):
    pos = 50
    zeros = 0
    
    def turn(current_pos, direction, steps):
        zero_passed=0
        if steps>99:
            zero_passed = steps//100
            steps = steps%100
                
        new_pos = current_pos + direction*steps
        if new_pos<0:
            if current_pos!=0:
                zero_passed += 1
            new_pos=100+new_pos
        elif new_pos>99:
            new_pos=new_pos-100
            if new_pos>0:
                zero_passed += 1
        
        return new_pos, zero_passed

    for direction, steps in [(-1 if line[0] == "L" else 1, int(line[1:])) for line in lines]:
        pos, zeros_passed  = turn(pos, direction, steps)
        if pos == 0: zeros += 1
        if count_zeros_passed: zeros += zeros_passed

    return (zeros)


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines,False)
    print(f"The result 1 is {result}.")
    result = solve(lines,True)
    print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
