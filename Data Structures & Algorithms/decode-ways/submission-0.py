class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0 for _ in range(len(s))]
        dp[0] = 1

        for index in range(1, len(s)):
            current_opportunities = 0

            # Check if the number you are is not zero -> this is your first opportunity
            # Then go back by 1
            # What you are doing in this opportunity is adding the 6 to it -> thus add the -1

            if s[index] != '0':
                current_opportunities += dp[index - 1]
                
            if s[index - 1] != '0' and 0 <= int(s[index - 1] + s[index]) <= 26:
                if index == 1:
                    current_opportunities += 1
                else:
                    current_opportunities += dp[index - 2]

            dp[index] = current_opportunities

        return dp[-1]