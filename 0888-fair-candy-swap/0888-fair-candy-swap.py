class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        diff = (sumB - sumA) // 2

        bobSet = set(bobSizes)

        for x in aliceSizes:
            if x + diff in bobSet:
                return [x, x + diff]