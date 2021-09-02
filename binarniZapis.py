n = int(input("Unesite n: \n"))

b = [0 for i in range(32)]
i = 0

while n > 0:
    b[i] = n % 2
    n = n // 2
    i += 1

print(b)