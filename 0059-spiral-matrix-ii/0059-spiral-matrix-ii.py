class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for j in range(n)] for i in range(n)]

        total = n*n
        count = 1

        left = 0
        right = n - 1

        top = 0
        bottom = n - 1

        while(count<=n*n):

            for j in range(left, right+1):
                matrix[top][j] = count
                count+=1

            top+=1

            if(top>bottom):
                break

            for i in range(top, bottom+1):
                matrix[i][right] = count
                count+=1

            right-=1

            if(left>right):
                break

            for j in range(right, left-1, -1):
                matrix[bottom][j] = count
                count+=1

            bottom-=1

            if(top>bottom):
                break

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = count
                count+=1

            left+=1

            if(left>right):
                break

        return matrix

