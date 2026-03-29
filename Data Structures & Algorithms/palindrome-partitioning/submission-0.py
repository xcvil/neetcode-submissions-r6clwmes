class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []
        
        def dfs(start):

            if start == len(s):
                res.append(subset.copy())
                return

            for end in range(start,len(s)):

                if s[start:end+1] == s[start:end+1][::-1]:
                    subset.append(s[start:end+1])            
                    dfs(end+1)
                    subset.pop()
                else:
                    continue
        
        dfs(0)
        return res


            

             