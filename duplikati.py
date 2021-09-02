def swap(a, i, j):
    pom = a[i]
    a[i] = a[j]
    a[j] = pom


a = [2, 1, 4, 5, 8, 5 , 4, 3, 0]

n = len(a)
i = 0

while i < n:
    if a[i] == a[a[i]]:
        i += 1
    else:
        swap(a, i, a[i])

duplikati = set()
for i in range(n):
    if a[i] != i:
        duplikati.add(a[i])

print(duplikati)
