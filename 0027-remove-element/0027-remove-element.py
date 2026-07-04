class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Pointer for the next position of a valid element
        k = 0  
        
        for i in range(len(nums)):
            # If the current element is NOT the value to remove
            if nums[i] != val:
                # Move it forward to the 'k' index
                nums[k] = nums[i]
                k += 1
                
        # k represents the count of elements that are not equal to val
        return k
