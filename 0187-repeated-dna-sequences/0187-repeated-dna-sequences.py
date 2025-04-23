class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        store = set()
        ans = set()
        for i in range(len(s)-9):
            word = s[i:i+10]
            if word in store and word not in ans:
                ans.add(word)
            store.add(word)
        return list(ans)
            