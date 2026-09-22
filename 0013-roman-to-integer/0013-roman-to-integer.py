class Solution:
    def romanToInt(self, s: str) -> int:
        value = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        total = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and value[s[i]] < value[s[i + 1]]:
                total -= value[s[i]]
            else:
                total += value[s[i]]
        return total
