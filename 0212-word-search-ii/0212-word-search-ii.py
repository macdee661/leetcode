from typing import List, Set

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix: str) -> TrieNode:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        # Build the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(node: TrieNode, x: int, y: int, path: str):
            if node.is_end_of_word:
                result.add(path)
                node.is_end_of_word = False  # Avoid duplicate words

            # Mark the cell as visited
            temp = board[x][y]
            board[x][y] = "#"

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] != "#":
                    new_char = board[new_x][new_y]
                    child_node = node.children.get(new_char)
                    if child_node:
                        dfs(child_node, new_x, new_y, path + new_char)

            # Unmark the cell
            board[x][y] = temp

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                start_char = board[i][j]
                child_node = trie.search_prefix(start_char)
                if child_node:
                    dfs(child_node, i, j, start_char)

        return list(result)
