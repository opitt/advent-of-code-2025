import os
import portion as P

def solve(intervals, ingredients):
    f=0
    for ingredient in ingredients:
        for interval in intervals:
            if int(ingredient) in interval:
                f+=1
                break
    
    return f

def solve2(intervals):
    merged = P.empty()
    for interval in intervals:
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
    intervals = [P.closed(int(a),int(b)) for a,b in [interval.split("-") for interval in lines[:idx]]]
    ingredients = lines[idx+1:]
  
    result = solve(intervals, ingredients)
    print(f"The result 1 is {result}.")
    result = solve2(intervals)
    print(f"The result 2 is {result}.")
    # 


#main(test=True)
main(test=False)
