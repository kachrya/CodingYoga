class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

        Note: The solution set must not contain duplicate triplets.

        For example, given array S = [-1, 0, 1, 2, -1, -4],

        A solution set is:
        [
            [-1, 0, 1],
            [-1, -1, 2]
        ]
        """
        nums = sorted(nums)
        ans = set()
        print(nums)
        for a_index in range(0, len(nums)-2):
            b_index = a_index+1
            c_index = len(nums)-1
            while b_index < c_index:
                print(a_index, b_index, c_index)
                if nums[a_index] + nums[b_index] + nums[c_index] == 0:
                    ans.add((nums[a_index], nums[b_index], nums[c_index]))
                    print(ans)
                    b_index += 1
                    c_index -= 1
                    # break
                elif nums[a_index] + nums[b_index] + nums[c_index] < 0:
                    b_index += 1
                else:
                    c_index -= 1
        print(ans)
        ans_list = []
        for i in ans:
            ans_list.append(list(i))
        print(list(ans_list))
        return list(ans_list)



soln = Solution()
#soln.threeSum([-1, 0, 1, 2, -1, -4])
#soln.threeSum([0, 0, 0, 0])
soln.threeSum([-2,0,1,1,2])
