class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        st = set()
        for i in word:
            if chr(ord(i) + 32) in word or chr(ord(i) - 32) in word:
                st.add(i.lower())
        return len(st)