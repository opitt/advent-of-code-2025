import os

def solve(paper_roll_map):
    rows = len(paper_roll_map)
    cols = len(paper_roll_map[0])

    rolls_to_move = 0
    for row in range(1,rows):
        for col in range(1,cols):
            # The forklifts can only access a roll of paper 
            # if there are fewer than four rolls of paper in the eight adjacent positions
            if paper_roll_map[row][col] == "@":
                rolls=""
                not_empty = sum(1 for x in (-1,0,1) for y in (-1,0,1) if paper_roll_map[row+x][col+y] in ("@", "X"))
                if not_empty - 1 < 4: # ignore the roll itself in the centre
                    rolls_to_move += 1
                    paper_roll_map[row][col] = "X"

    # move the marked paper rolls
    for row in range(1,rows):
        for col in range(1,cols):
            if paper_roll_map[row][col] == "X":
                paper_roll_map[row][col] = "."

    return rolls_to_move


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    # enhance the map with empty fields to make the scanning simpler
    lines.insert(0,"."*len(lines[0]))
    lines.append("."*len(lines[0]))
    lines = [list("."+line+".") for line in lines]

    # how many paper rolls can be moved?
    result = solve(lines)
    print(f"The result 1 is {result}.")
    while True:
       # keep moving until nothing can be moved
       moved = solve(lines)
       if not moved: break
       result+=moved
    print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
