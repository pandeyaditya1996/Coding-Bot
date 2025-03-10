class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix)
        cols = len(matrix[0])

        count = 0
        total = rows*cols

        top = 0
        bottom = rows - 1

        left = 0
        right = cols - 1

        ans = []

        while(count<rows*cols):

            for i in range(left,right+1):
                ans.append(matrix[top][i])
                count+=1

            top+=1

            if top>bottom:
                break

            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
                count+=1

            right-=1

            if left>right:
                break            

            for i in range(right,left - 1, -1):
                ans.append(matrix[bottom][i])
                count+=1

            bottom-=1

            if top>bottom:
                break

            for i in range(bottom,top - 1, -1):
                ans.append(matrix[i][left])
                count+=1

            left+=1

            if left>right:
                break

        return ans
