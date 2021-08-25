def find_outlier(integers):
    n = integers
    even = n
    count = 0
    for i in n:
        if i % 2 != 0:
            count += 1
            if count <len(n):
                for j in n:
                    if j % 2 != 0:
                        return j
        elif i % 2 == 0:
            count += 1
            if count <len(n):
                for j in n:
                    if j % 2 == 0:
                        return j

print(find_outlier([2, 4, 6, 8, 10, 3])) #op 3
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36])) #op 11
print(find_outlier([160, 3, 1719, 19, 11, 13, -21])) #op 160
