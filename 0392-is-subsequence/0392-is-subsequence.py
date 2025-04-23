class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        idx_s = 0
        if not s:
            return True
        for idx_t in range(len(t)):
            if t[idx_t] == s[idx_s]:
                idx_s+=1
            if idx_s == len(s):
                return True
        
        return False
            