class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def buildHash(s: str) -> list:
            arr = [0]*26
            for i in s:
                arr[ord(i)-ord('a')] += 1
            return str(arr)
        new_strs = [buildHash(i) for i in strs]
        tableHash = {}
        for n in range(len(new_strs)):
            if new_strs[n] in tableHash:
                tableHash[new_strs[n]].append(n)
            else:
                tableHash[new_strs[n]] = [n]

        return [[strs[n] for n in i] for i in tableHash.values()]
