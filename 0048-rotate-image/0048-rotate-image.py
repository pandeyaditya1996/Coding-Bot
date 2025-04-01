class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(i,cols):
                print(matrix[i][j], matrix[j][i])
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(rows):
            left = 0
            right = cols - 1
            while(left<right):
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left+=1
                right-=1

                