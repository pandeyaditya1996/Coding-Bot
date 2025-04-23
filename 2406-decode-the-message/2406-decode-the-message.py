class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        store = 'abcdefghijklmnopqrstuvwxyz'
        alpha_store = {" ":" "}

        idx = 0
        for char in key:
            if char not in alpha_store:
                alpha_store[char] = store[idx]
                idx+=1
                if idx==26:
                    break

        ans = ""
        for char in message:
            ans+=alpha_store[char]

        return ans