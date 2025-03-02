class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ptr1 = 0
        ptr2 = 0
        ans = ""
        while(ptr1<len(word1) and ptr2<len(word2)):
            ans+=word1[ptr1]+word2[ptr2]
            ptr1+=1
            ptr2+=1

        while(ptr1<len(word1)):
            ans+=word1[ptr1]
            ptr1+=1
        while(ptr2<len(word2)):
            ans+=word2[ptr2]
            ptr2+=1

        return ans

        