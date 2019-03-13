a, b = [set((input().split())) for _ in range(4)][1::2]

results = []

for num in b.intersection(a):
    a.discard(num)
    b.discard(num)

results = sorted(map(int, a.union(b)))

for num in results:
    print(num)
