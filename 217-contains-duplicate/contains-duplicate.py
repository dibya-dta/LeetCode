class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        sort_nums = sorted(nums)
        for i, item in enumerate(sort_nums):
            if len(sort_nums) > i+1 and sort_nums[i] == sort_nums[i + 1]:
                return True
        return False
