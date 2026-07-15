class Solution:
    def checkSubarraySum(self, nums, k):
        remainder_map = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            if k != 0:
                total %= k

            if total in remainder_map:
                if i - remainder_map[total] > 1:
                    return True
            else:
                remainder_map[total] = i

        return False