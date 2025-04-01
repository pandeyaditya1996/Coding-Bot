class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])

        ans = []
        count = 0

        top = 0
        bottom = rows - 1

        left = 0
        right = cols - 1

        while(count<rows*cols):

            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top+=1

            if top>bottom:
                break

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right-=1

            if left>right:
                break

            for j in range(right, left - 1, -1):
                ans.append(matrix[bottom][j])
            bottom-=1

            if top>bottom:
                break

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left+=1

            if left>right:
                break

        return ans