MAX_VALUE = 10**9 + 1

def dot_prod(xs, ys):
    return sum(x*y for x, y in zip(xs, ys))

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index):
        while index <= self.size:
            self.tree[index] += 1
            index += index & -index

    def query(self, index):
        count = 0
        while index > 0:
            count += self.tree[index]
            index -= index & -index
        return count

def compress_arr(arr):
    arr_set = set(arr)
    for x in arr:
        if 2 * x < MAX_VALUE:
            arr_set.add(2 * x)
        arr_set.add(x // 2)
    sorted_arr = sorted(arr_set)
    return {value: index + 1 for index, value in enumerate(sorted_arr)}


n = int(input())
shelf = list(map(int, input().split()))

compressed_shelf = compress_arr(shelf)

max_val = len(compressed_shelf)

left_tree = FenwickTree(max_val)
right_tree = FenwickTree(max_val)

left_count = [0] * len(shelf)
right_count = [0] * len(shelf)

for i in range(len(shelf)):
    query_val = compressed_shelf.get(shelf[i] * 2, max_val + 1) - 1
    left_count[i] = left_tree.query(max_val) - left_tree.query(query_val)
    left_tree.update(compressed_shelf[shelf[i]])

for i in range(len(shelf) - 1, -1, -1):
    query_val = compressed_shelf.get(shelf[i] // 2, 0)
    right_count[i] = right_tree.query(query_val)
    right_tree.update(compressed_shelf[shelf[i]])

print(dot_prod(left_count, right_count))
