class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cc = defaultdict(lambda: 0)
        licensePlate = licensePlate.lower()
        tc = 0
        for c in licensePlate:
            if c.isalpha():
                cc[c] += 1
                tc += 1

        words = sorted(words, key = lambda word:len(word))
        print(words)

        for word in words:
            ccw = cc.copy()
            tcw = tc
            if len(word) < tc:
                continue
            for c in word:
                if c in ccw and ccw[c] > 0:
                    ccw[c] -= 1
                    tcw -= 1
            if tcw == 0:
                return word
        return ""

        