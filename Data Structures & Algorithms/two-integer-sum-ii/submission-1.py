class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:

            if numbers[r] == (target-numbers[l]):
                return [l+1, r+1]
            elif numbers[r] > (target-numbers[l]):
                r -= 1
            elif numbers[r] < (target-numbers[l]):
                l += 1