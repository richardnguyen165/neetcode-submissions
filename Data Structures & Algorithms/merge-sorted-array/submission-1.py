class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        First solution:

        Simply find the positions of each element from nums2 in nums1
        Then we need to shift based on those positions

        Let the first pointer be at 0, responsible for tracking position in nums1
        Let the second pointer be at 0, responsible for tracking position in nums2

        First loop, while first pointer is less than the length of nums1,
        and the second pointer is less than the length of nums2, create an equivalent list
        and copy the elements into there
        '''

        nums_1_pointer, nums_2_pointer, copy_list, copy_list_pointer = 0, 0, [0] * (m + n), 0

        while (nums_1_pointer < m and nums_2_pointer < n):
            if nums2[nums_2_pointer] <= nums1[nums_1_pointer]:
                copy_list[copy_list_pointer] = nums2[nums_2_pointer]
                nums_2_pointer += 1
            else:
                copy_list[copy_list_pointer] = nums1[nums_1_pointer]
                nums_1_pointer += 1
            copy_list_pointer += 1

        while nums_1_pointer < m:
            copy_list[copy_list_pointer] = nums1[nums_1_pointer]
            copy_list_pointer += 1
            nums_1_pointer += 1
        
        while nums_2_pointer < n:
            copy_list[copy_list_pointer] = nums2[nums_2_pointer]
            copy_list_pointer += 1
            nums_2_pointer += 1

        for index, number in enumerate(copy_list):
            nums1[index] = number