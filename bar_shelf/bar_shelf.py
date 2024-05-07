import bisect
from sortedcontainers import SortedList

def dot_prod(xs, ys):
    return sum(x*y for x, y in zip(xs, ys))

def count_double_prefix(arr):
    prefix = SortedList()
    counts = []
    for x in arr:
        index = bisect.bisect_left(prefix, 2*x)
        count = len(prefix) - index
        counts.append(count)
        bisect.insort(prefix, x)
    return counts

def count_half_suffix(arr):
    suffix = SortedList()
    counts = []
    for x in reversed(arr):
        index = bisect.bisect_right(suffix, x//2)
        counts.append(index)
        bisect.insort(suffix, x)
    counts.reverse()
    return counts

    
n = int(input())

shelf = list(map(int, input().split()))

prefixes = count_double_prefix(shelf)
suffixes = count_half_suffix(shelf)

print(dot_prod(prefixes, suffixes))
