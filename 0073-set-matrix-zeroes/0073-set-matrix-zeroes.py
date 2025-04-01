class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        row_set = set()
        col_set = set()

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0





                

        