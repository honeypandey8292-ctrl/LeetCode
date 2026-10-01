class Solution:
    def isValid(self, s: str) -> bool:

        Stack=[]
        mapping={")":"(","}":"{","]":"["}
        for char in s:
            if char in mapping:
                top_element= Stack.pop() if Stack else "#"
                #agar maching eliment nahi mila to 
                if mapping[char] != top_element:
                    return False
            else:
                Stack.append(char)

        return not Stack                



        