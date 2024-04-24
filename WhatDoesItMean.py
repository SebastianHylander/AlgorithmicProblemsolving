n, name = input().split()

# Indices 0-25 correspond to a-z, index 26 holds the possible value
trie = [[0]*27]
valIndex = 26

# Convert character a-z to int 0-25
def num(c): 
    return ord(c) - 97

# Get the value (number of meanings) associated with the node
def val(node):
    return trie[node][valIndex]

# Read input
for _ in range(int(n)):
    word,v = input().split()
    node = 0
    
    # Move though trie, and add nodes if necessary
    for c in word:
        if trie[node][num(c)] == 0:
            trie[node][num(c)] = len(trie)
            trie.append([0]*27)
        node = trie[node][num(c)]
    # Insert the value at the end of the word
    trie[node][valIndex] = int(v)


name = list(map(num,name))

# Value at index k is the number of possible meanings from index k in name
totals = ([0]*len(name))+[1]

# Used to check for matches from the given startIndex in the name.
def check(node,startIndex,nextIndex):
    # If the current node has a value in the trie,
    # update the total for startIndex, using the total for nextIndex.
    if val(node) > 0:
        totals[startIndex] = (totals[startIndex] + val(node)*totals[nextIndex]) % 1_000_000_007
    # Move to next node in trie, if matching.
    if nextIndex < len(name) and trie[node][name[nextIndex]] > 0:
        check(trie[node][name[nextIndex]], startIndex, nextIndex+1)

# Find number of possible meanings from each index in name, in reverse order.
for i in range(len(name)-1,-1,-1):
    check(0,i,i)

print(totals[0])