class Solution:
    def reverseDegree(self, s: str) -> int:
        count = 0
        total = 0
        for i, c in enumerate(s, 1):

            Str1 = 26 - (ord(c) - ord("a"))
            count =i
            total = (count * Str1) + total

        return total
