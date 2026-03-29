class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        # Step 1: Count frequencies - O(n)
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: create bucket - O(n)
        for n, c in count.items():
            freq[c].append(n)
        # Step 3: Collect top k from highest frequency - O(n)
        result = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        

