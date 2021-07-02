matrix = input().split(',')
p = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'P':
            p.append([i,j])
print(abs(p[0][0]-p[1][0])+abs(p[0][1]-p[1][1]))