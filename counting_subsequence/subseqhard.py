t = int(input())

for i in range(t):
    count = 0
    foundsum = {0: 1}
    input()
    input()
    sequence = list(map(int, input().split()))
    for i in range(len(sequence)):
        if i == 0:
            foundsum[sequence[i]] = 1
            if sequence[i] == 47:
                count += 1
            continue
        sequence[i] += sequence[i - 1]
        foundsum[sequence[i]] = foundsum.get(sequence[i], 0) + 1
        count += foundsum.get(sequence[i] - 47, 0)

    print(count)
