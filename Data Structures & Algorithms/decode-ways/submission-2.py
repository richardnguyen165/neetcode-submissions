class Solution:
    def numDecodings(self, s: str) -> int:
        # You cannot decode a leading zero
        # You cannot decode a zero

        if s[0] == '0':
            return 0
        
        cache = {}

        # Top-Down implementation

        # Base Cases:

        cache[0] = 1
        if len(s) > 1:
            two_length = 0
            current_string = s[0:2]
            if s[1] != '0':
                two_length += 1
            if 0 <= int(current_string) <= 26:
                two_length += 1
            cache[1] = two_length

        def top_decoding(current_index):
            # Two ways, go back by one (meaning we start at current)
            #
            if current_index < 0:
                return 0

            total = 0
            if current_index in cache:
                return cache[current_index] # Represents how many ways you can decode the string [0:current_index + 1]
            
            # Case 1: only consider the current index, and go back only back by one
            if s[current_index] != '0':
                total += top_decoding(current_index - 1)
        

            # Case 2:
            if s[current_index - 1] != '0' and 0 <= int(s[current_index - 1: current_index + 1]) <= 26:
                total += top_decoding(current_index - 2)

            cache[current_index] = total

            return total
        

        return top_decoding(len(s) - 1)
