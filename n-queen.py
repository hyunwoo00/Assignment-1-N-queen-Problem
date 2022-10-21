n = int(input("Enter the number of queens: "))
result = []
def printBoard(result):
    count = 0
    for i in range(len(result)):

        if i == 10:
            break
        for j in range(1,n+1):
            index = result[i].index(j)
            for k in range(n):
                if k == index:
                    print("1",end= " ")
                else:
                    print("0", end = " ")
            print()
            
            
        print()


    
 
def isSafe(board, row, col):
    for i in range(col):
        if (board[row][i]):
            return False
 
    i = row
    j = col
    while i >= 0 and j >= 0:
        if(board[i][j]):
            return False
        i -= 1
        j -= 1
 

    i = row
    j = col
    while j >= 0 and i < n:
        if(board[i][j]):
            return False
        i +=1
        j -= 1
 
    return True

 
def solveNQUtil(board, col):
    if (col == n):
        res = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    res.append(j+1)
        result.append(res)
    
        return True

    res2 = False
    for i in range(n):

        if (isSafe(board, i, col)):
 

            board[i][col] = 1
            res2 = solveNQUtil(board, col + 1) or res2
            board[i][col] = 0
 

    return res2
 

 
 
def solveNQ(n):
    result.clear()
    board = [[0 for i in range(n)]
             for j in range(n)]
    solveNQUtil(board, 0)
    result.sort()
    return result

 

result = solveNQ(n)
print("Total possible arrangements:",len(result))
print("The first few (not more than 10) arrangements are:")
printBoard(result)



 
