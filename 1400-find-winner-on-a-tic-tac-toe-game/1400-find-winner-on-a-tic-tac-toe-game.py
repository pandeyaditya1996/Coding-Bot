class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        def diagonalCheck(matrix, player):
            if matrix[0][0] == matrix[1][1] == matrix[2][2] or matrix[0][2] == matrix[1][1] == matrix[2][0]:
                return player

        def rowCheck(matrix, player):
            for row in matrix:
                if row in [["o","o","o"],["x","x","x"]]:
                    return player

        def colCheck(matrix, player):
            first_col = (matrix[0][0] == matrix[1][0] == matrix[2][0])
            second_col = (matrix[0][1] == matrix[1][1] == matrix[2][1])
            third_col = (matrix[0][2] == matrix[1][2] == matrix[2][2])

            if first_col or second_col or third_col:
                return player

        matrix = [[1,2,3],[4,5,6],[7,8,9]]

        count = 0

        for i,j in moves:
            player = "A" if count%2 ==0 else "B"
            matrix[i][j] = "x" if player == "A" else "o"
            checker = rowCheck(matrix,player) or colCheck(matrix,player) or diagonalCheck(matrix, player)
            if checker:
                print(matrix)
                return checker
            count+=1

        print(matrix)
        return "Draw" if len(moves)==9 else "Pending"