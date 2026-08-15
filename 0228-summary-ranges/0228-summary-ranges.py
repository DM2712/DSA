class Solution(object):
    def summaryRanges(self, nums):
        ans = []
        n = len(nums)

        if n == 0:
            return ans

        start = nums[0]

        for i in range(n):

            if i == n - 1 or nums[i + 1] != nums[i] + 1:

                if start == nums[i]:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + "->" + str(nums[i]))

                if i + 1 < n:
                    start = nums[i + 1]

        return ans