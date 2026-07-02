class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters_of_s = {}
        letters_of_t = {}

        for index in range(0, len(s)):
            s_letter = s[index]
            t_letter = t[index]
            if s_letter in letters_of_s:
                letters_of_s[s_letter] += 1
            else:
                letters_of_s[s_letter] = 1
            
            if t_letter in letters_of_t:
                letters_of_t[t_letter] += 1
            else:
                letters_of_t[t_letter] = 1

        return letters_of_s == letters_of_t
        
        