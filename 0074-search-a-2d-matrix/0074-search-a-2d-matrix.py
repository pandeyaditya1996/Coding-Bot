class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows - 1
        while(left<=right):
            mid = (left + right)//2
            elem = matrix[mid][0]
            if elem==target:
                return True
            elif elem>target:
                right = mid - 1
            else:
                left = mid + 1

        if mid==0 and target<elem:
            return False

        if mid<rows-1 and target>matrix[mid+1][0]:
            search = mid + 1
        elif mid>0 and target<matrix[mid][0]:
            search = mid - 1
        else:
            search = mid

        print(search, mid)

        l = 0
        r = cols - 1

        while(l<=r):
            mid = (l + r)//2
            elem = matrix[search][mid]
            if elem == target:
                return True
            elif elem>target:
                r = mid - 1
            else:
                l = mid + 1

        return False
            