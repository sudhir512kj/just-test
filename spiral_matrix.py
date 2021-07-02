def spiralOrder(matrix):
    ans = []

    if (len(matrix) == 0):
        return ans

    R = len(matrix)
    C = len(matrix[0])
    rowBeg = 0
    colBeg = 0
    rowEnd = R-1
    colEnd = C-1

    while rowBeg <= rowEnd and colBeg <= colEnd:
        for i in range(colBeg, colEnd+1):
            ans.append(matrix[rowBeg][i])
        rowBeg += 1

        for i in range(rowBeg, rowEnd+1):
            ans.append(matrix[i][rowEnd])
        
        colEnd -= 1

        if rowBeg <= rowEnd:
            for i in range(colEnd, colBeg-1, -1):
                ans.append(matrix[rowEnd][i])
        rowEnd -= 1

        if colBeg <= colEnd:
            for i in range(rowEnd, rowBeg-1, -1):
                ans.append(matrix[i][colBeg])
        colBeg += 1
    
    return ans
        


# Driver code
a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

print(spiralOrder(a))


