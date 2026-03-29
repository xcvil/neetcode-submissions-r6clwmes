class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        nums_len = len(nums)
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue

            l, r = i+1, nums_len-1
            while l < r:
                threeSum = nums[l]+nums[r]+num
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l<r:
                        l += 1
        return res