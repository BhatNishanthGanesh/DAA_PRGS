# 9.Design and implement for a given chess board having N×N cells, place N queens on the board in such a way that no queen attacks any other
# queen. If it is possible to place all the N queens in such a way that no queen attacks another queen, then print N lines having N Queens.
# If there is more than one solution of placing the queens, print all of them. If it is not possible to place all N queens in the desired way,
# then print "Not possible".


def isSafe(board,row,col,n):
    for i in range(row):
        if board[i][col]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,-1,-1),range(col,n)):
        if board[i][j]==1:
            return False
    return True

def solve_n_queens_util(board,row,n,solutions):
    if row==n:
        solutions.append([row[:] for row in board])
        return
    else:
        for col in range(n):
            if isSafe(board,row,col,n):
                board[row][col]=1
                solve_n_queens_util(board,row+1,n,solutions)
                board[row][col]=0
def solve_n_queens(n):
    solutions=[]
    board=[[0 for _ in range(n)] for _ in range(n)]
    solve_n_queens_util(board,0,n,solutions)
    return solutions

def printSolutions(solutions):
    if not solutions:
        print("No solutions: ")
    else:
        for sol in solutions:
            for row in sol:
                print(''.join(map(str,row)))
            print()
            
N=int(input("Enter the value of N: "))
queen_solutions=solve_n_queens(N)
printSolutions(queen_solutions)
    