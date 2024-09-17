from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def diff_by_one(word1, word2):
            count = 0
            for index in range(len(word1)):
                if word1[index] != word2[index]:
                    count +=1
                    if count > 1:
                        return False
            return True if count == 1 else False
        
        count = 0
        queue = deque([beginWord])
        visited = set()

        while queue:
            count += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                visited.add(word)

                if word == endWord:
                    return count

                for new_word in wordList :
                    if diff_by_one(new_word, word) and new_word not in visited:
                        queue.append(new_word)
                        visited.add(new_word)
        return 0
            


