class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

        Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

        Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

        Example:
        Input: [1,2,1,2,6,7,5,1], 2
        Output: [0, 3, 5]
        Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
        We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
        Note:
        nums.length will be between 1 and 20000.
        nums[i] will be between 1 and 65535.
        k will be between 1 and floor(nums.length / 3).
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Best single, double, and triple sequence found so far
        bestSeq = 0
        bestDoubleSeq = [0, k]
        bestTripleSeq = [0, k, k * 2]

        # Sums of each window
        seqSum = sum(nums[0:k])
        seqTwoSum = sum(nums[k:k * 2])
        seqThreeSum = sum(nums[k * 2:k * 3])

        # Sums of combined best windows
        bestSeqSum = seqSum
        bestTwoSum = seqSum + seqTwoSum
        bestThreeSum = seqSum + seqTwoSum + seqThreeSum

        # Current window positions
        # starts from 1 because we will compare this against
        # window 0
        seqIndex = 1
        twoSeqIndex = k  + 1
        threeSeqIndex = k * 2  + 1
        print(nums)
        print("Windows %d %d %d" % (seqIndex, twoSeqIndex, threeSeqIndex))
        print("seqsum %d %d %d\n-----------" % (seqSum, seqTwoSum, seqThreeSum))

        while threeSeqIndex <= len(nums) - k:
            # Update the three sliding windows
            print("Windows %d %d %d" % (seqIndex, twoSeqIndex, threeSeqIndex))
            seqSum = seqSum - nums[seqIndex - 1] + nums[seqIndex + k - 1]
            seqTwoSum = seqTwoSum - nums[twoSeqIndex - 1] + nums[twoSeqIndex + k - 1]
            seqThreeSum = seqThreeSum - nums[threeSeqIndex - 1] + nums[threeSeqIndex + k - 1]
            print("seqsum %d %d %d" % (seqSum, seqTwoSum, seqThreeSum))
            # Update best single window
            if seqSum > bestSeqSum:
                bestSeq = seqIndex
                bestSeqSum = seqSum

            # Update best two windows
            if seqTwoSum + bestSeqSum > bestTwoSum:
                bestDoubleSeq = [bestSeq, twoSeqIndex]
                bestTwoSum = seqTwoSum + bestSeqSum

            # Update best three windows
            if seqThreeSum + bestTwoSum > bestThreeSum:
                bestTripleSeq = bestDoubleSeq + [threeSeqIndex]
                bestThreeSum = seqThreeSum + bestTwoSum

            # Update the current positions
            seqIndex += 1
            twoSeqIndex += 1
            threeSeqIndex += 1
            print("best seq %r" % (bestTripleSeq))

        print(bestTripleSeq)
        return bestTripleSeq


soln = Solution()
soln.maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)