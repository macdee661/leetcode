class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def unique(str1, str2):
            letters = set()
            for char in str1:
                letters.add(char)
            for char in str2:
                if char not in letters:
                    letters.add(char)
                else:
                    return False
            return True

        def dfs(res, arr):
            if not arr:
                return res
            res2 = ''
            if unique(res, arr[0]):
                res2 = res + arr[0]

            string1 = dfs(res, arr[1:])
            string2 = dfs(res2, arr[1:])

            if len(string1) > len(string2):
                return string1
            return string2

        return len(dfs('', arr))