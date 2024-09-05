class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        letters = {}
        start = 0
        max_len = 0
        for index in range(len(s)):
            letter = s[index]
            if letter in letters and letters[letter] >= start:
                start = letters[letter] + 1
            letters[letter] = index

            max_len = max(max_len, index-start+1)

        return max_len

















#hashmap keeps track of indices of the right most character of each mype.
#when we get to a duplicate, we set the start the position after the initial instance of that letter, updating out window,
#if we dont we compute the new max, and keep going
        
        