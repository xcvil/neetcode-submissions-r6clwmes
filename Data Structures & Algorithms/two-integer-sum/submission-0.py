class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tableHash = {}
        for i in range(len(nums)):
            if target - nums[i] in tableHash:
                return [tableHash[target-nums[i]], i]
            else:
                tableHash[nums[i]] = i