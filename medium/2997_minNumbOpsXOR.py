#2997: Minimum Number of Operations to make XOR ...
class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Check if XOR of array returns k
        xor = 0
        for num in nums:
            xor ^= num

        if xor == k:
            return 0
        
        # Converting ints to big enough bits is not failproof (look to optimize)
        count=0
        binK= format(k, '0100b')
        binXOR= format(xor, '0100b')
        for bit in range(len(binXOR)):
            if binK[bit] != binXOR[bit]:
                count+=1
        
        return count

        