from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
for i in range(n):
    d[input()].append(i + 1)

for _ in range(m):
    element = input()
    indices = d[element]
    if indices:
        print(" ".join(map(str, indices)))
    else:
        print(-1)
