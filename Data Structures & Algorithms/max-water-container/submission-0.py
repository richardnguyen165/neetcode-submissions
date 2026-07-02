class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_height = 0 
        start, end = 0, len(heights) - 1

        while start < end:
            max_height = max(min(heights[start], heights[end]) * (end - start), max_height)

            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1

        return max_height