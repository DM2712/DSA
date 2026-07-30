class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """

        # Sort scores in descending order
        sorted_score = sorted(score, reverse=True)

        # Store score -> rank
        rank = {}

        for i in range(len(sorted_score)):
            if i == 0:
                rank[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank[sorted_score[i]] = "Bronze Medal"
            else:
                rank[sorted_score[i]] = str(i + 1)

        # Create answer in original order
        ans = []

        for s in score:
            ans.append(rank[s])

        return ans