def spiralRotate(mat, M, N, k):
    temp = []
    m = M
    n = N
    s = 0
    l = 0

    start = temp[0]
    tIdx = 0

    while s < m and l < n:
        end = start

        for i in range(l,n):
            temp[tIdx] = mat[s][i]
            end += 1
            tIdx += 1
        s += 1

        for i in range(s,m):
            temp[tIdx] = mat[i][n-1]
            end += 1
            tIdx += 1
        n -= 1

        if s < m:
            for i in range(n-1, l-1, -1):
                temp[tIdx] = mat[i][l]
                end += 1
                tIdx += 1
            l += 1

        if end-start > k:
            temp[:k] = reversed(temp[:k])
            temp[k:] = reversed(temp[k:])
            temp = reversed(temp)
            start = end
        else:
            break