import time

RED = True
BLACK = False

class RBNode:
    def __init__(self, key, color, left=None, right=None, parent=None):
        self.key = key
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent
        self.size = 1

    @staticmethod
    def isRed(node):
        return node is not None and node.color == RED

    @staticmethod
    def size(node):
        return 0 if not node else node.size

def put(node, value):
    if not node:
        return RBNode(key = value, color = RED)

    cmp = node.key - value
    if cmp > 0:
        node.left = put(node.left, value)
    elif cmp < 0:
        node.right = put(node.right, value)
    else:
        node.size += 1

    if RBNode.isRed(node.right) and not RBNode.isRed(node.left):
        node = rotateLeft(node)

    if RBNode.isRed(node.left) and RBNode.isRed(node.left.left):
        node = rotateRight(node)

    if RBNode.isRed(node.left) and RBNode.isRed(node.right):
        flipColors(node)

    node.size = 1 + RBNode.size(node.left) + RBNode.size(node.right)

    return node

def rotateRight(node):
    x = node.left
    node.left = x.right
    x.right = node
    x.color = node.color
    node.color = RED
    x.size = node.size
    node.size = RBNode.size(node.left) + RBNode.size(node.right) + 1
    return x

def rotateLeft(node):
    x = node.right
    node.right = x.left
    x.left = node
    x.color = node.color
    node.color = RED
    x.size = node.size
    node.size = RBNode.size(node.left) + RBNode.size(node.right) + 1
    return x

def flipColors(node):
    node.color = not node.color
    node.left.color = not node.left.color
    node.right.color = not node.right.color

def rank(node, key):
    if not node:
        return 0
    cmp = node.key - key
    if cmp < 0:
        return 1 + RBNode.size(node.left) + rank(node.right, key)
    elif cmp > 0:
        return rank(node.left, key)
    else:
        return RBNode.size(node.left) + 1

def dot_prod(xs, ys):
    return sum(x*y for x, y in zip(xs, ys))

def count_double_prefix(arr):
    prefix = None
    counts = []
    for x in arr:
        count = RBNode.size(prefix) - rank(prefix, 2*x-1)
        counts.append(count)
        prefix = put(prefix, x)
    return counts

def count_half_suffix(arr):
    suffix = None
    counts = []
    for x in reversed(arr):
        count = rank(suffix, x//2)
        counts.append(count)
        suffix = put(suffix, x)
    counts.reverse()
    return counts


n = int(input())

shelf = list(map(int, input().split()))


prefixes = count_double_prefix(shelf)
suffixes = count_half_suffix(shelf)

print(dot_prod(prefixes, suffixes))
