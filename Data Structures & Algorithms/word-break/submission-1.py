class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Note: it has to include every single letter
        '''
        C(k) := can you form the word include the kth letter
        using the words provided in the dictionary.

        do we recursively do this?

        ok, iterate it through each letter, forming a stack until we form a word

        We can either accept a word, or keep going

        Return true, if each letter is covered in some way

        Return false, if at least one letter is not covered at all

        (But how do we do iteratively?)

        Cases: the letter you are on is either part of a entire word,
        part of some sub word or is a word itself
        '''

        dp = [False for _ in range(len(s))]
        current_stack = ""
        for i, letter in enumerate(s):
            if i == 0:
                dp[i] = letter in wordDict
                current_stack += letter
                continue
            
            current_stack += letter
            if (letter in wordDict) or (current_stack in wordDict):
                dp[i] = True
                continue
            for j in range(0, i):
                if dp[j] and s[j + 1: i + 1] in wordDict:
                    dp[i] = True
                    break
            
        print(dp)
        return dp[-1]
            

        


