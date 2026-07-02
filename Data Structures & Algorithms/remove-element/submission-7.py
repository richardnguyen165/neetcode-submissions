class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # simple

        temp = []
        
        for number in nums:
            if number != val:
                temp.append(number)
        for index, number in enumerate(temp):
            nums[index] = temp[index]
        return len(temp)