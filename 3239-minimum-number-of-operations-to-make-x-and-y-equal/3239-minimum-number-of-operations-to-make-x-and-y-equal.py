from collections import deque
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        nums = set()
        queue = deque([x])
        count = -1

        while len(queue) > 0:
            count += 1
            for _ in range(len(queue)):
                num  = queue.popleft()
                if num == y:
                    return count
                if num not in nums:
                    nums.add(num)
                    if num % 11 == 0:
                        queue.append(num / 11)
                    if num % 5 == 0:
                        queue.append(num / 5)
                    queue.append(num - 1)
                    queue.append(num + 1)


        

