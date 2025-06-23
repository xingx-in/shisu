a = [2, 3, 7, 5, 3, 5, 2, 9]
m = max(a)
b = [0] * (m + 1)
for i in range(len(a)):
    n = a[i]
    b[n] += 1
for j in range(len(b)):
    if b[j] == 1:
        print(j)
