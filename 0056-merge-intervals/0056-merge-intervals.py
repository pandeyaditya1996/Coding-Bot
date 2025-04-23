class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        first = intervals[0][0]
        second = intervals[0][1]

        ans = []
        for initial,final in intervals[1:]:
            if initial>second:
                ans.append([first,second])
                first = initial
                second = final
            else:
                first = min(first,initial)
                second = max(second, final)
        ans.append([first,second])
        return ans