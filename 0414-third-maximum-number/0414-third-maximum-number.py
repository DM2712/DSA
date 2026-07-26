class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = list(set(nums))
        n.sort(reverse=True)

        if len(n)>=3:
            return n[2]
        else:
            return n[0]