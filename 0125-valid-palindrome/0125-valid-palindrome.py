class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        cleandata= [char.lower() for char in s if char.isalnum()]

        return cleandata == cleandata[::-1]
        