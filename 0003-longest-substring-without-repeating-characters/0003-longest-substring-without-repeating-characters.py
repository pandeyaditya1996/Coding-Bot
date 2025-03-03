class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        store = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while(s[right] in store):
                store.remove(s[left])
                left+=1
            store.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
                
     