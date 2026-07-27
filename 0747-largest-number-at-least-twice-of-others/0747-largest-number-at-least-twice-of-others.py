class Solution(object):
    def dominantIndex(self, nums):
        n1 = nums[:]
        n1.sort(reverse=True)

        if n1[0] >= 2 * n1[1]:
            return nums.index(n1[0])

        return -1