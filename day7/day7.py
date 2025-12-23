import os

def solve(manifold):
    splits = 0
    beams = {manifold[0].index("S")}
    max_beam = len(manifold[0])-1
    for row in manifold[1:]:
        new_beams = set()
        for beam in beams:
            if row[beam] == ".":
                row[beam] = "|"
                new_beams.add(beam)
            if row[beam] == "^":
                splits+=1
                if beam-1>=0:
                    new_beams.add(beam-1)
                    row[beam-1] = "|"
                if beam+1<=max_beam:
                    new_beams.add(beam+1)
                    row[beam+1] = "|"
        beams = new_beams

    return splits

def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = [line.strip("\n") for line in lines]

    #
    manifold = [list(line) for line in lines]
    result = solve(manifold)
    print(f"The result 1 is {result}.")

    #result = solve2(numbers, operators)
    #print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
