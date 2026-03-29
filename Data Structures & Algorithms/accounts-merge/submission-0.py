class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                graph[email].add(i)

        def dfs(email):
            if email in visited:
                return

            visited.add(email)
            curr.append(email)

            for account in graph[email]:
                for em in accounts[account][1:]:
                    dfs(em)
            return

        res = []
        start = 0
        visited = set()
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in visited:
                    curr = []
                    dfs(email)
                    res.append([account[0]] + sorted(curr))

        return res