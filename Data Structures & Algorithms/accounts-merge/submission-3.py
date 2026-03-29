class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for account in accounts:
            first = account[1]
            for email in account[2:]:
                graph[first].add(email)
                graph[email].add(first)


        def dfs(email):
            if email in visited:
                return 

            visited.add(email)
            curr.append(email)

            for nei in graph[email]:
                dfs(nei)

            return None

        visited = set()
        res = []
        for account in accounts:
            if account[1] not in visited:
                curr = []
                dfs(account[1])
                res.append([account[0]]+sorted(curr))

        return res
