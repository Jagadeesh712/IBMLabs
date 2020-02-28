
x=  [[12,3,5],
    [3,4,5],
    [6,7,8]]
y=  [[5,6,7,8],
    [1,2,3,2],
    [1,1,1,1]]
result= [[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result [i][j] += x[i][k]*y[k][j]
for r in result:
    print(r)