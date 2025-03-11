class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        first = intervals[0][0]
        second = intervals[0][1]
        ans = []
        for x,y in intervals[1:]:
            if x>second:
                ans.append([first, second])
                first = x
            second = max(y, second)
        
        ans.append([first, second])
        return ans



