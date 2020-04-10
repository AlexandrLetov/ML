list_one = [1, 2, 3, 4, 5, 6, 7]
list_two = [5, 6, 7, 8, 9, 10, 11]

flag = False

for item in list_one:
    if item in list_two:
        flag = True

print(flag)