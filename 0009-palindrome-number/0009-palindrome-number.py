class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        p1, p2 = 0, len(num_str) -1

        while p2 >= p1:

            if num_str[p2] != num_str[p1]:
                return False
            
            p1 += 1
            p2 -= 1
        return True
    
