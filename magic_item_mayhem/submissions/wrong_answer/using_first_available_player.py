#!/usr/bin/env python3
n,m = map(int,input().split())

players = dict()

for _ in range(n):
    players[input().strip()] = [0]*5

for _ in range(m):
    inp = input().split()
    cat = int(inp[0])
    for name in inp[1:]:
        if players[name][cat] == 0 and sum(players[name]) < 3:
            players[name][cat] = 1
            break

print(sum(players.values()))