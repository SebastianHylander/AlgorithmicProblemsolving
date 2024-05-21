import random, string, edmonds_karp_for_gen

# Replace 
# 1 <= N <= 50 
N = 10
# 1 <= M <= 300
M = 10

filename = '../magic_item_mayhem/data/secret/' + str(N) + '_' + str(M) + '_Full'

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

# Generate items
for _ in range(M):
    cat = random.randint(1,5)
    fin.write(str(cat) + ' ' + ' '.join(names) + '\n')

fin.close()

# Run algorithm and write answer file
res = edmonds_karp_for_gen.run(filename)

fans = open(filename + '.ans', "x")
fans.write(str(res) + '\n')
fans.close()