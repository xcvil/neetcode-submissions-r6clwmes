class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for i in count:
            freq[count[i]].append(i)
        ans = []
        for i in freq[::-1]:
            ans.extend(i)
            if len(ans) == k:
                return ans
        

