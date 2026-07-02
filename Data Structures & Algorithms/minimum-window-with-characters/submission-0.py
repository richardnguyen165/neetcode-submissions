class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def freqHelper(word):
            freq_send = {}
            for letter in word:
                if letter in freq_send:
                    freq_send[letter] += 1
                else:
                    freq_send[letter] = 1
            return freq_send
        
        def verifyMakeWord(test, standard):
            for key, value in test.items():
                if key not in standard:
                    return False
                if standard[key] < test[key]:
                    return False
            return True

        '''
        Ok 
        1. Make right pointer go all the way to the right, until we get all characters from t possible
        2. If we get all characters from t, we reduce the left pointer until its not possible.
        3. We can do this by checking both hashmaps as a frequency counter, and then loop through the t hashmap to check values
        4. Keep comparing lengths to get smallest one
        5. Return a varibale contains a string
        6. Loop will terminate when right pointer equates to the len(s)
        '''
        if s == t:
            return s
        if len(t) > len(s):
            return ""
        
        t_freq = freqHelper(t)
        print(t_freq)

        result_string = ""
        left_pointer = 0
        current_freq = {}
        for right_pointer in range(0, len(s)):

            current_char = s[right_pointer]

            if current_char in current_freq:
                current_freq[current_char] += 1
            else:
                current_freq[current_char] = 1
            
            result = verifyMakeWord(t_freq, current_freq);
            print(0, result, current_freq)
            if (len(s[left_pointer:right_pointer + 1]) < len(result_string) or not result_string) and result:
                result_string = s[left_pointer:right_pointer + 1]
            print(result_string)
        
            while result and left_pointer < right_pointer:
                left_pointer += 1
                remove_char = s[left_pointer - 1]

                if current_freq[remove_char] == 1:
                    del current_freq[remove_char]
                else:
                   current_freq[remove_char] -= 1

                result = verifyMakeWord(t_freq, current_freq)
                print(1, result, current_freq)
                if ((len(s[left_pointer:right_pointer + 1]) < len(result_string) or not result_string)) and result:
                    result_string = s[left_pointer:right_pointer + 1]
                print(result_string)
                print(left_pointer, right_pointer)
                print("-")
            
            print(left_pointer, right_pointer)
            print("-")

        return result_string