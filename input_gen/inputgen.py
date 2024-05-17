import random, string, edmonds_karp_for_gen

# Replace 
# 1 <= N <= 100 
N = 100 
# 1 <= M <= 600
M = 600

filename = 'magic_item_mayhem/data/secret/' + str(N) + '_' + str(M)

fin = open(filename + '.in', "x")

fin.write(str(N) + ' ' + str(M) + '\n')

# Generate names
names = set()
while len(names) < N:
    length = random.randint(3,10)
    name = ''.join(random.choices(string.ascii_lowercase, k=length))
    names.add(name)

names = list(names)

for name in names:
    fin.write(name + '\n')

# Makes it more likely to have fewer names per item
numbers = range(1,N+1)
weights = [x**N for x in range(N,0,-1)]

# Generate items
for _ in range(M):
    cat = random.randint(1,5)
    selected = random.sample(names, k=random.choices(numbers, weights=weights, k=1)[0])
    fin.write(str(cat) + ' ' + ' '.join(selected) + '\n')

fin.close()

# Run algorithm and write answer file
res = edmonds_karp_for_gen.run(filename)

fans = open(filename + '.ans', "x")
fans.write(str(res) + '\n')
fans.close()