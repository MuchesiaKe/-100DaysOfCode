nested_list = [
    ["John", "Dennis", "Brian", "Kevin"],
    ["Sharon", "Irene", "Carol", "Mary"],
    [344, 455, 234, 87, 23, 43],
    [45995],
    [21.453]
]
for row in nested_list:
    for column in row:
        print(column)