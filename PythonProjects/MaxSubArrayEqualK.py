class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

        Note:
        The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

        Example 1:
        Given nums = [1, -1, 5, -2, 3], k = 3,
        return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

        Example 2:
        Given nums = [-2, -1, 2, 1], k = 1,
        return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

        Follow Up:
        Can you do it in O(n) time?
        """
        subarr_len = 0
        running_sum = 0
        my_dict = {0: -1} # whenever running sum is 0, value at my_dict[0] remains -1. this is good
        # because we want consecutive values in sub array that total to 0 inorder to get longest
        # subarray that totals to k

        # What made running sum increase?
        # If it increased by "k", that means
        # there are elements that sum to exactly
        # "k" in between.
        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum not in my_dict:
                my_dict[running_sum] = i
            if running_sum-k in my_dict:
                # if true, running sum increased by k
                subarr_len = max(subarr_len, i-my_dict[running_sum-k])
            print(my_dict)
        return subarr_len



soln = Solution()
print(soln.maxSubArrayLen([1, 2, 3, 4, 2, 9, 3, 6], 9))
              #running sum 1  3  6  10 12 21 24 30