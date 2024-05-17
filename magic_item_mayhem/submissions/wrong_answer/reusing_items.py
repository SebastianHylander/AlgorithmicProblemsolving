#!/usr/bin/env python3
n,m = map(int, input().split())

players = dict()

for _ in range(n):
    players[input().strip()] = [0]*5

for _ in range(m):
    inp = input().split()
    cat = int(inp[0])-1
    for name in inp[1:]:
        players[name][cat] = 1

print(sum(min(3,sum(x)) for x in players.values()))