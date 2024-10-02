class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {}
        rank = 1
        sorted_arr = sorted(arr)
        for num in sorted_arr:
            if num not in ranks:
                ranks[num] = rank
                rank += 1

        for index in range(len(arr)):
            arr[index] = ranks[arr[index]]

        return arr
        