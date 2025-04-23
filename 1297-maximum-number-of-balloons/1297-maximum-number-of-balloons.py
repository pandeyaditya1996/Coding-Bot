class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        store = Counter(text)
        return min(store['a'],store['n'],store['b'],store['l']//2,store['o']//2)