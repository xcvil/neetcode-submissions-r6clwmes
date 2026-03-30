class Solution:
    def calcEquation(self, equations, values, queries):
        graph = collections.defaultdict(dict)

        for (a, b), v in zip(equations, values):
            # graph[a][a] = 1
            # graph[b][b] = 1
            graph[a][b] = v
            graph[b][a] = 1 / v

        # 传递闭包：如果 a→k 和 k→b 都已知，推出 a→b
        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]

        return [graph[a].get(b, -1)
                for a, b in queries]