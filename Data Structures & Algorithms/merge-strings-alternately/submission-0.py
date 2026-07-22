class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word, word1len, word2len = "", 0, 0
        while word1len < len(word1) and word2len < len(word2):
            new_word += word1[word1len] + word2[word2len]
            word1len, word2len = word1len + 1, word2len + 1
        
        while word1len < len(word1):
            new_word += word1[word1len]
            word1len += 1

        while word2len < len(word2):
            new_word += word2[word2len]
            word2len += 1
            
        return new_word