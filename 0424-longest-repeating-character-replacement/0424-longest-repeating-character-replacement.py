from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        store = defaultdict(int)
        left = 0
        ans = 0
        max_f = 1
        for right in range(len(s)):
            store[s[right]]+=1
            max_f = max(max_f, store[s[right]])
            if right-left+1 - max_f<=k:
                ans = max(ans, right-left+1)
            else:
                store[s[left]]-=1
                left+=1
        return ans
        

        

        
        