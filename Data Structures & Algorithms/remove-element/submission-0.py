class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Points to the spot where the next valid element should go
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Overwrite with valid number
                k += 1             # Move write pointer forward
                
        return k  # Number of valid elements

        