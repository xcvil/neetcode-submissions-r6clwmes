class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []

        def dfs(open_count, close_count):
            if open_count == close_count == n:
                res.append("".join(subset))
                return
            # if open_count == n or close_count == n:
            #     return
            if open_count < n:
                subset.append("(")
                dfs(open_count + 1, close_count)
                subset.pop()
            if open_count > close_count:
                subset.append(")")
                dfs(open_count, close_count + 1)
                subset.pop()

        dfs(0,0)
        return res