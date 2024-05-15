from copy import deepcopy
n, m = map(int, input().split())

prefs = {}

for i in range(n):
    prefs[input().strip()] = [0,[]]

items = []

for i in range(m):
    item = input().split()
    items.append(item[0])
    for name in item[1:]:
        prefs[name][1].append(i)


def combine(names, items, combinations=[]):
    if items == []:
        return combinations
    item = items.pop(0)     
        
    for combination in deepcopy(combinations):
        for name in names:
            new_combination = deepcopy(combination)
            new_combination[name].append(item)
            combinations.append(new_combination)
    for name in names:
        comb = {}
        for name2 in names:
            comb[name2] = []
        comb[name].append(item)
        combinations.append(comb)
        
    
    return combine(names, items, combinations)

combinations = combine(prefs.keys(), [i for i in range(m)])     

max_value = 0
for combination in combinations:
    valid = True
    for name, items in combination.items():
        holding = set()
        for item in items:
            if item in holding or item not in prefs[name][1]:
                valid = False
                break
            holding.add(item)
        
        if len(holding) > 3:
            valid = False
            break
    if valid:
        value = sum([len(items) for items in combination.values()])
        if value > max_value:
            max_value = value

print(max_value)