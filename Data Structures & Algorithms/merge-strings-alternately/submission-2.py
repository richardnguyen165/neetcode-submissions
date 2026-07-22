class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Only one loop
        res = []
        w1c, w2c = 0, 0
        while w1c < len(word1) or w2c < len(word2):
            if w1c < len(word1):
                res.append(word1[w1c])
                w1c += 1
            if w2c < len(word2):
                res.append(word2[w2c])
                w2c += 1
        
        return "".join(res)