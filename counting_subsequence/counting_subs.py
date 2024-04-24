t = int(input())

for _ in range(t):
    count = 0
    foundsum = {0: 1}
    input()
    input()
    sequence = list(map(int, input().split()))
    current_sum = 0
    for x in sequence:
        current_sum += x
        count += foundsum.get(current_sum - 47, 0)
        foundsum[current_sum] = foundsum.get(current_sum, 0) + 1

    print(count)


