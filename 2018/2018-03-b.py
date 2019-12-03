from aocd import data, submit


suit = {}
fabrics = set()
for fab in data.split("\n"):
    fab  = fab.split(" ")
    id   = int(fab[0].replace("#", ""))
    x, y = map(int, fab[2][:-1].split(","))
    w, t = map(int, fab[3].split("x"))
    fabrics.add(id)
    
    for yy in range(y, y+t): 
        for xx in range(x, x+w):
            pt = (xx, yy)
            if pt in suit: 
                suit[pt].add(id)
                fabrics -= suit[pt]
            else:
                suit[pt] = {id}
                                
result = min(fabrics)
print("result", result)
submit(result)

