class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(set)

        for (var1, var2), value in zip(equations, values):
            graph[var1].add((var2, value))
            graph[var2].add((var1, 1/value))

        def dfs(start, end, accumulates):
            if start not in graph or end not in graph:
                return None

            if start == end:
                return accumulates
            visited.add(start)
            for nei, cnv in graph[start]:
                if nei not in visited:
                    res = dfs(nei, end, accumulates*cnv)
                    if res is not None:
                        return res

            return None

        ans = []
        for start, end in queries:
            visited = set()
            res = dfs(start, end, 1)
            if res is None:
                ans.append(-1)
            else:
                ans.append(res)

        return ans
