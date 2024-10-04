class Solution:
    def longestPalindrome(self, s: str) -> int:

        string = sorted(s)
        print(f'string is {string}')
        new_stack = []
        count = 0
        for i in string:
            if not new_stack:
                new_stack.append(i)
            elif new_stack[-1] == i:
                new_stack.pop()
                count = count + 1
            else:
                new_stack.append(i)



        if count == 0:
            return 1
        elif new_stack:
            return 2 * count + 1
        else:
            return 2 * count
