#维度 dimension/dim
#two dimension list

lMatrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

lMatrix[1][0] = 10
print(lMatrix[1][0])

for row in lMatrix:
    for item in row:
        print(item)