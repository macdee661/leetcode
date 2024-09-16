keyboard = {
"2": "abc",
"3": "def",
"4": "ghi",
"5": "jkl",
"6": "mno",
"7": "pqrs",
"8": "tuv",
"9": "wxyz"
}
from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        def back_track(index, string):
            if index == len(digits):
                res.append(string)
                return
            
            word = keyboard[digits[index]]

            for letter in word:
                back_track(index + 1, string + letter)
        back_track(0, "")
        return res




        