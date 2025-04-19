class Solution:
    def minOperations(self, s: str) -> int:
        
        count = 0
        for i in range(len(s)):
            if i%2!=int(s[i]):
                count+=1
        
        return min(count,len(s) - count)