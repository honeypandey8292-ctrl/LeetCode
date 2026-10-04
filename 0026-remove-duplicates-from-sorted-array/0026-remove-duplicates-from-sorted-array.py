class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # 'i' pointer track karega last unique element ka index
        i = 0
        
        # 'j' pointer pure array ko traverse karega
        for j in range(1, len(nums)):
            # Agar koi naya unique element milta hai
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
                
        # Total unique elements 'i + 1' honge
        return i + 1
        


