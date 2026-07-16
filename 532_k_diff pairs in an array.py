class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums.sort()
        count = 0

        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] - nums[i] == k:
                    count += 1
                    break
                elif nums[mid] - nums[i] < k:
                    left = mid + 1
                else:
                    right = mid - 1

        return count