class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = set()
        left = 0
        ans = 0
        for i in range(len(s)):
            if s[i] not in store:
                store.add(s[i])
            else:
                ans = max(ans,i - left)
                while(s[left]!=s[i]):
                    store.remove(s[left])
                    left+=1
                left+=1
        return max(ans, len(s)-left)

                
     