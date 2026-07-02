class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group_anagrams_dictionaries = {}

        for word in strs:
            sorted_split_word = ''.join(sorted(word))
            if sorted_split_word not in group_anagrams_dictionaries:
                group_anagrams_dictionaries[sorted_split_word] = [word]
            else:
                list_copy_anagram = group_anagrams_dictionaries[sorted_split_word]
                list_copy_anagram.append(word)
                group_anagrams_dictionaries[sorted_split_word] = list_copy_anagram
               
        return group_anagrams_dictionaries.values()
