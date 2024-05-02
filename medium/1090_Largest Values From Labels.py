# 1090. Largest Values From Labels
class Solution(object):
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type numWanted: int
        :type useLimit: int
        :rtype: int
        """

        items = sorted(zip(values, labels), reverse=True)
        s = 0
        count = 0
        label_count = {}

        for value, label in items:
            if count == numWanted:
                break
            if label_count.get(label, 0) < useLimit:
                s += value
                label_count[label] = label_count.get(label, 0) + 1
                count +=1

        return s
