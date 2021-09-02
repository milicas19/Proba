a = [1, 5, -4, 6, 0, 5, 0, -8, 2, 0]

i = 0
n = len(a)
j = n - 1

k = 0

while k < j:
    if a[k] < 0:
        pom = a[i]
        a[i] = a[k]
        a[k] = pom
        i += 1
        k += 1
    if a[k] > 0:
        pom = a[j]
        a[j] = a[k]
        a[k] = pom
        j -= 1
    if a[k] == 0:
        k += 1

print(a)
        
