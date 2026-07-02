class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_categories = {}
        all_split_categories = []
        counter = 0
        for word in strs:
            letter_count = {}
            for letter in word:
                if letter not in letter_count:
                    letter_count[letter] = 1
                else:
                    letter_count[letter] += 1
            if letter_count not in all_split_categories:
                all_split_categories.append(letter_count)
                new_list = []
                new_list.append(word)
                all_categories[counter] = new_list
                counter += 1
            else:
                index_of_anagram = all_split_categories.index(letter_count)
                current_words = all_categories.get(index_of_anagram).copy()
                current_words.append(word)
                all_categories[index_of_anagram] = current_words
        return list(all_categories.values())