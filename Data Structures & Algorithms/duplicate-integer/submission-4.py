class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        all_ns = set()
        for n in nums:
            if n in all_ns:
                return True
            all_ns.add(n)
        return False