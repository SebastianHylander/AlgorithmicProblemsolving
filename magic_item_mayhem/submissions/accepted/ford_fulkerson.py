from collections import defaultdict
import math
class Node:
    def __init__(self):
        self.adj = defaultdict(int)
        self.fromNode = None
    
    def updateEdge(self, other, cap):
        self.adj[other] = self.adj[other] + cap
    
def ford_fulkerson(start, end):
    result = 0

    while bfs(start, end):
        node = end
        path_cap = end.fromNode.adj[end]
        while node != start:
            path_cap = min(path_cap,node.fromNode.adj[node])
            node = node.fromNode
        
        node = end
        while node != start:
            node.fromNode.updateEdge(node, -path_cap)
            # Update shared capacity if it exists
            if (node.fromNode, node) in shared_cap:
                shared_cap[(node.fromNode, node)][0].updateEdge(shared_cap[(node.fromNode, node)][1], -path_cap)

            node.updateEdge(node.fromNode, path_cap)
            # Update shared capacity if it exists
            if (node, node.fromNode) in shared_cap:
                shared_cap[(node, node.fromNode)][0].updateEdge(shared_cap[(node, node.fromNode)][1], path_cap)

            node = node.fromNode
        result = result + path_cap
    return result

def bfs(start, end):
    marked = defaultdict(bool)
    queue = [start]
    marked[start] = True

    while len(queue) > 0:
        node = queue.pop(0)
        if node == end:
            return True
        for neighbour, cap in node.adj.items():
            if (not marked[neighbour]) and cap > 0:
                queue.append(neighbour)
                marked[neighbour] = True
                neighbour.fromNode = node
    return False

n, m, t = map(int, input().split())

start_node = Node()
end_node = Node()

shared_cap = {}

characters = {}

for _ in range(n):
    name = input().strip()
    attune_node = Node()
    not_attune_node = Node()
    start_node.updateEdge(attune_node, 3)
    start_node.updateEdge(not_attune_node, math.inf)

    attune_types = [Node() for _ in range(t)]
    not_attune_types = [Node() for _ in range(t)]

    for i in range(t):
        attune_node.updateEdge(attune_types[i], 1)
        not_attune_node.updateEdge(not_attune_types[i], 1)

        shared_cap[(attune_node, attune_types[i])] = (not_attune_node, not_attune_types[i])
        shared_cap[(not_attune_node, not_attune_types[i])] = (attune_node, attune_types[i])

    characters[name] = (attune_types, not_attune_types)
        

input()

for i in range(m):
    item = Node()
    item.updateEdge(end_node, 1)
    item_info = input().split()

    item_type = int(item_info[0])
    attune = item_info[1]
    item_characters = item_info[2:]

    for character in item_characters:
        if attune == 'A':
            characters[character][0][item_type].updateEdge(item, 1)
        else:
            characters[character][1][item_type].updateEdge(item, 1)

print(ford_fulkerson(start_node, end_node))
    