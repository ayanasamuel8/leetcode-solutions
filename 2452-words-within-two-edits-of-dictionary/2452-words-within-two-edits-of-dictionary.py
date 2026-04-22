
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        def diff(w1, w2):
            n = len(w1)
            cnt = 0
            for i in range(n):
                if w1[i] != w2[i]:
                    cnt += 1
            return cnt
        words = []
        for word in queries:
            for w in dictionary:
                if diff(word, w) <= 2:
                    words.append(word)
                    break
        return words