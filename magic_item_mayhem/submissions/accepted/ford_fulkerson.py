#!/usr/bin/env python3
from collections import defaultdict
n,m = map(int, input().split())

source = 0
sink = -1
graph = defaultdict(dict)
id = 0
players = dict()

for _ in range(n):
    playerid = id+1
    players[input().strip()] = playerid
    # add edge source to player
    graph[source][playerid] = 3
    graph[playerid][source] = 0
    # add edges player to categories
    for i in range(1,6):
        graph[playerid][playerid+i] = 1
        graph[playerid+i][playerid] = 0
    id += 6

for _ in range(m):
    id += 1
    inp = input().split()
    cat = int(inp[0])
    # add edge item to sink
    graph[id][sink] = 1
    graph[sink][id] = 0
    # add edges category to item
    for name in inp[1:]:
        graph[players[name]+cat][id] = 1
        graph[id][players[name]+cat] = 0

def dfs(path):
    visited = {source}
    queue = [source]
    while queue:
        node = queue.pop()
        for next in graph[node]:
            if next not in visited and graph[node][next] > 0:
                path[next] = node
                if next == sink:
                    return True
                visited.add(next)
                queue.append(next)
    return False

path = dict()
while dfs(path):
    node = sink
    while node != source:
        next = path[node]
        graph[node][next] += 1
        graph[next][node] -= 1
        node = next

print(sum(graph[sink].values()))