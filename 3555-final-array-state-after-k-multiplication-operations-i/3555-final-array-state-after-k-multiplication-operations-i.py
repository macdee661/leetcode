class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        nums_dict = {}
        for index, number in enumerate(nums):
            nums_dict[index] = number
        for _ in range(k):
            sorted_nums = sorted(nums_dict.items(), key=lambda x: (x[1], x[0]))
            index, value = sorted_nums[0][0], sorted_nums[0][1]
            nums_dict[index] = value * multiplier
        return [x[1] for x in nums_dict.items()]
        
        
        