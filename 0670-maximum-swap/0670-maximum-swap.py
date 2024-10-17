class Solution:
    def maximumSwap(self, num: int) -> int:

        num_str = [letter for letter in str(num)]
        p1 = 0
        print(num_str)

        for index in range(0, len(num_str)-1):
            p1 = index + 1
            min_index = float('inf')
            while p1 < len(num_str):
                if int(num_str[p1]) > int(num_str[index]):
                    if min_index == float('inf'):
                        min_index = p1
                    else: 
                        if int(num_str[p1]) >= int(num_str[min_index]):
                            print(f"min index is now {min_index}")
                            min_index = p1
                p1 += 1

            if min_index != float('inf'):
                num_str[index], num_str[min_index] = num_str[min_index], num_str[index]
                return int(''.join(num_str))
        return num

        