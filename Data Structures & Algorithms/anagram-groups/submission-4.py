class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        charCount = defaultdict(list)
        for s in strs:
            key = [0]*26
            for i in s:
                key[ord(i)-ord('a')] += 1
            key = tuple(key)
            charCount[key].append(s)
        return list(charCount.values())
