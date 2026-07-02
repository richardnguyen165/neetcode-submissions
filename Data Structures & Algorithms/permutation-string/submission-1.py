class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def processChars(word):
            freq_counter = {}
            for character in word:
                if character not in freq_counter:
                    freq_counter[character] = 1
                else:
                    freq_counter[character] += 1
            return freq_counter
        
        # Fixed window?
        max_length_of_first = len(s1)
        s1_freq = processChars(s1)
        
        moving_freq = {}
        first_pointer = 0
        second_pointer = max_length_of_first - 1

        while second_pointer < len(s2):
            current_word = s2[first_pointer:second_pointer + 1]
            if not first_pointer:
                moving_freq = processChars(current_word)
            else:
                char_to_remove = s2[first_pointer - 1]
                char_to_add = current_word[-1]

                if moving_freq[char_to_remove] - 1 == 0:
                    del moving_freq[char_to_remove]
                else:
                    moving_freq[char_to_remove] -= 1

                if char_to_add not in moving_freq:
                    moving_freq[char_to_add] = 1
                else:
                    moving_freq[char_to_add] += 1

            if moving_freq == s1_freq:
                return True
            first_pointer += 1
            second_pointer += 1
            print(current_word, moving_freq)
        
        return False

        