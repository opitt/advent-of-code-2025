import os
import portion as P

def solve(fresh, ingredients):
    FRESH = [range(a,b+1) for a,b in (list(map(int,f.split("-"))) for f in fresh)]
    f=0
    for ingredient in ingredients:
        for fresh_range in FRESH:
            if int(ingredient) in fresh_range:
                f+=1
                break
    
    return f

def solve2(fresh):
    
    merged = P.closed
    FRESH_intervals = [P.closed(int(a),int(b)) for a,b in [f.split("-") for f in fresh]]
    
    merged = P.empty()
    for interval in FRESH_intervals:
        merged = merged | interval

    fresh_articles=0
    for atomic in merged:
        fresh_articles += atomic.upper - atomic.lower + 1
        
    return fresh_articles

def main(test):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(
        os.path.join(script_path, "test.txt" if test else "input.txt"), encoding="utf-8"
    ) as input:
        lines = input.readlines()
    lines = list(map(str.strip, lines))

    #
    idx = lines.index("")
    fresh = lines[:idx]
    ingredients = lines[idx+1:]
  
    result = solve(fresh, ingredients)
    print(f"The result 1 is {result}.")
    result = solve2(fresh)
    print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
