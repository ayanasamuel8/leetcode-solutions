class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cntr = Counter(word)
        n = len(word)
        seen = set()
        flagged = set()
        for i in word:
            cntr -= Counter([i])
            if i not in flagged and chr(ord(i) - 32) in cntr and i not in cntr:
                seen.add(i)
            if i.isupper() and i.lower() in cntr:
                flagged.add(i.lower())
        return len(seen)