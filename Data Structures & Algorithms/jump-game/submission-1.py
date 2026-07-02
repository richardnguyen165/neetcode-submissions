class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Bottom-up

        if len(nums) == 1:
            return True

        # Ok, we just need to check if we can reach the end

        all_squares = [-1 for _ in range(len(nums))]
        all_squares[0] = 0

        # We will put the index from which the previous square jumps to
        # Run time O(n^2)
        for index_one in range(1, len(nums)):
            # We can walk to it or, we need to jump to it
            for index_two in range(0, len(nums)):
                if (index_one != index_two) and (nums[index_two] != 0) and (all_squares[index_two] != -1) and (index_two == index_one - 1 or index_two + nums[index_two] >= index_one):
                    all_squares[index_one] = index_two
                    break

        print(all_squares)
        return True if all_squares[-1] != -1 else False