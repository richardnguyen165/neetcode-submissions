class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        def checkIfAbleReplace():
            total = freq_map["total"]
            for key, value in freq_map.items():
                if (total - value <= k) and key != 'total':
                    return True
            return False

        # Sliding window + hashmap
        if len(s) == 1:
            return s

        # hashmap consists of total of the amount of letters, and for each letter how many they are
        freq_map = {"total": 0}

        start_pointer, best_length = 0, 0

        for end_pointer in range(0, len(s)):
            end_pointer_character = s[end_pointer]

            if (end_pointer_character in freq_map):
                freq_map[end_pointer_character] += 1
            else:
                freq_map[end_pointer_character] = 1
            freq_map["total"] += 1
            print()
            print(freq_map)

            if (end_pointer - start_pointer) >= k:
                result = checkIfAbleReplace()
                while not result and start_pointer < end_pointer:
                    starter_pointer_character = s[start_pointer]
                    freq_map[starter_pointer_character] -= 1
                    if (freq_map[starter_pointer_character] == 0):
                        del freq_map[starter_pointer_character]
                    freq_map["total"] -= 1
                    start_pointer += 1

                    result = checkIfAbleReplace()
                if result:
                    best_length = max(best_length, end_pointer - start_pointer + 1)
            else:
                best_length = max(best_length, end_pointer - start_pointer + 1)
            print(start_pointer, end_pointer + 1, best_length, freq_map)

        return best_length