class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x< 0:
            return False
        if x < 10:
            return True
        num_str = str(x)
        p1, p2 = 0, len(num_str) -1

        while p2 >= p1:

            if num_str[p2] != num_str[p1]:
                return False
            
            p1 += 1
            p2 -= 1
        return True
    
