import os

def solve(battery_packs, jolts_needed):
    pack_joltages = []
    for joltages in [list(map(int, batteries)) for batteries in battery_packs]:
        pack = ""
        need = jolts_needed
        while need:
            if len(joltages)==need:
                need=0
                pack += "".join(map(str,joltages))
            else:
                j1 = max(joltages[-need:-(len(joltages)+1):-1])
                pack += str(j1)
                need -= 1
                idx1 = joltages.index(j1)
                joltages = joltages[idx1+1:]
                
        pack_joltages.append(int(pack)) 

    return sum(pack_joltages)


def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    result = solve(lines, 2)
    print(f"The result 1 is {result}.")
    result = solve(lines, 12)
    print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
