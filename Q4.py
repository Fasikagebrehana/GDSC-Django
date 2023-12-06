total, count = 0, 0
for i in range(1, 51):
    if i % 2 == 0:
        total += i
        if i % 3 == 0:
            print("Three")
            count += 1
        elif i % 5 == 0:
            print("Five")
            count += 1
        else:
            print(i)
print(total, count)
    