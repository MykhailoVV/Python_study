def snail(snail_map):
    n = len(snail_map)
    res = snail_map[0]
    directon = 1
    x = n - 1
    j = n - 1
    i = 0
    while x > 0:
        for b in range(x):
            i = i + directon
            res.append(snail_map[i][j])
        directon = directon * (-1)
        for b in range(x):
            j = j + directon
            res.append(snail_map[i][j])
        x -= 1
    return res

arr = [[1, 2, 3], [4, 5, 6 ], [7, 8, 9]]

print(snail(arr))
