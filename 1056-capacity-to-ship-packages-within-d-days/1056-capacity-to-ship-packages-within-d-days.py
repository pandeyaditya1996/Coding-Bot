import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(mid):
            count = 1
            curr = 0
            for w in weights:
                if curr + w >mid:
                    count+=1
                    curr = w
                else:
                    curr+=w
            return count<=days

        totalWt = 0
        maxWt = float('-inf')
        for w in weights:
            maxWt = max(w, maxWt)
            totalWt+=w

        l = maxWt
        r = totalWt

        ans = r
        while(l<=r):

            mid = (l+r)//2
            if check(mid):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid+1
        
        return ans