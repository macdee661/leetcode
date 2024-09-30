class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []

        for index, temperature in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < temperature:
                next_i = stack.pop()
                res[next_i] =  index - next_i
            stack.append(index)
        
        return res



        