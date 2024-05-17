#!/usr/bin/env python3
n,m = map(int,input().split())

players = dict()

for i in range(n):
    players[input().strip()] = i*5

itemtypes = []
itemusers = []

for _ in range(m):
    inp = input().split()
    itemtypes.append(int(inp[0])-1)
    itemusers.append([players[name] for name in inp[1:]])

highestFound = 0

stack = [(0,[0]*5*n)]

while stack:
    index,combination = stack.pop()

    if index == m:
        highestFound = max(highestFound, sum(combination))
    else:
        # for each player who can use the item
        for player in itemusers[index]:
            # if the player is not already using an item in the same category
            # and the player is not already using 3 items
            if combination[player+itemtypes[index]] == 0 and sum(combination[player:player+5]) < 3:
                # let the player use the item, and go to the next item
                newcombination = list(combination)
                newcombination[player+itemtypes[index]] = 1
                stack.append((index+1,newcombination))
        # let no one have it
        stack.append((index+1,combination))

print(highestFound)
