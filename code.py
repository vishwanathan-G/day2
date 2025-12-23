a = [10, 20, 30, 40, 50, 60, 70]
remove = [20, 40, 60]

for val in remove:
    while val in a:
        a.remove(val)
print(a)
