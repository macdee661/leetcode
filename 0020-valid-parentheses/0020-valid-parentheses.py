class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = set(["(", "{", "["])
        for letter in s:
            if letter in opens:
                stack.append(letter)
            else:
                if not stack: return False
                closing = stack.pop()
                if letter == "}" and closing != "{":
                    return False
                elif letter == ")" and closing != "(":
                    return False
                elif letter == "]" and closing != "[":
                    return False
        if not stack:
            return True
        return False