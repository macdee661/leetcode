class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the list
        # if the complement is in the set, add the pair,
        # else, add the number to the set
        complements = {}
        res = []
        for index, num in enumerate(nums):
            comp = target - num
            if comp in complements:
                return [index, complements[comp]]
            else:
                complements[num] = index

        

        