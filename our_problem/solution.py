n, m = map(int, input().split())


names = []
for _ in range(n):
    names.append(input().strip())


items = []
max_value = 0
for i in range(m):
    item = input().split()
    value = int(item.pop(0))
    max_value = max(max_value, value)
    item_value = (value, set())
    for name in item:
        item_value[1].add(name)
    items.append(item_value)

preferences = []

for item in items:
    preferences.append([])
    for _ in range(3):
        for name in names:
            if name in item[1]:
                preferences[-1].append(max_value-item[0])
            else:
                preferences[-1].append(max_value)
        
        
for lst in preferences:
    print(lst)