class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        left_max = height[left]
        right = len(height) - 1
        right_max = height[right]
        total_water = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                total_water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                total_water += right_max - height[right]

        return total_water




        


