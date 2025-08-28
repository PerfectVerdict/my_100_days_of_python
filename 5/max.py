integers = [1, 4, 2, 5, 6, 3, 7]
lowest = 0
ordered_list = []
for int in integers:
    if int >= lowest:
        lowest = int
        ordered_list.append(int)
    else:
        pass
print(ordered_list)
