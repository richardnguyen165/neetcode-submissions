class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            "1": "",
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def get_all(digit_index = 0, current_letter = ""):
            if digits == "":
                return []
            
            if len(current_letter) == len(digits):
                return [current_letter]
            
            results = []
            get_number = digits[digit_index]
            get_letters = number_map[get_number]
            for letter in get_letters:
                copy_of_current_letter = current_letter[:]
                copy_of_current_letter += letter
                results.extend(get_all(digit_index + 1, copy_of_current_letter))
            
            return results
        
        return get_all()