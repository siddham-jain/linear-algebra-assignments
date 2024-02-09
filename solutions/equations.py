def solve(A, b):
    row, column = len(A), len(A[0])
    if row != column:
        return -1
   
    AM = [row + [b[i]] for i, row in enumerate(A)]
    for i in range(column):
        maxrow = max(range(i, row), key=lambda j: abs(AM[j][i]))
        AM[i], AM[maxrow] = AM[maxrow], AM[i]

        if abs(AM[i][i]) < 1e-10:
            return -2

        AM[i] = [elem / AM[i][i] for elem in AM[i]]

        for j in range(i + 1, row):
            factor = AM[j][i]
            AM[j] = [elem_j - factor * elem_i for elem_i, elem_j in zip(AM[i], AM[j])]

    ans = [0] * column
    for i in range(column - 1, -1, -1):
        ans[i] = AM[i][column]
        for j in range(i + 1, column):
            ans[i] -= AM[i][j] * ans[j]

    return ans


def det(A):
    row, col = len(A), len(A[0])
    if row != col:
        return 0
    if col == 1:
        return A[0][0]
    determinant = 0
    for i in range(col):
        submat = [[A[j][k] for k in range(col) if k != i] for j in range(1, col)]
        determinant += (-1) ** i * A[0][i] * det(submat)

    return determinant