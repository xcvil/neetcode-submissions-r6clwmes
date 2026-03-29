class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def buildHash(s: str) -> tuple:
            arr = [0] * 26
            for c in s:
                arr[ord(c) - ord('a')] += 1
            return tuple(arr)  # tuples are hashable
        
        tableHash = {}
        for s in strs:
            key = buildHash(s)
            if key in tableHash:
                tableHash[key].append(s)
            else:
                tableHash[key] = [s]
        
        return list(tableHash.values())
