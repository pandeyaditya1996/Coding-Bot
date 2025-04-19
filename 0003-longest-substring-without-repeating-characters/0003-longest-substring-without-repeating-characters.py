class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:



        left = 0
        store = set()
        ans = 0
        for right in range(len(s)):
            while(s[right] in store):
                store.remove(s[left])
                left+=1
            ans = max(ans, right-left+1)
            store.add(s[right])

        return ans