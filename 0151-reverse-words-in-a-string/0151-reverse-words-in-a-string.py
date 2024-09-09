class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ''
        index = 0
        while index < len(s):
            if not s[index].isalnum():
                index +=1
            else:
                while index < len(s) and s[index].isalnum():
                    word = word + s[index]
                    index += 1
                words.append(word)
                word = ''
        return " ".join(words[::-1])

