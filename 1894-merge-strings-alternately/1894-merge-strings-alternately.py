class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        string = []
        length = max(len(word1), len(word2))

        for index in range(length):
            if index < len(word1):
                string.append(word1[index])
            if index < len(word2):
                string.append(word2[index])
        return "".join(string)