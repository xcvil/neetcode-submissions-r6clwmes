class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pa] = pb

        for account in accounts:
            for email in account[1:]:
                if email not in parent:
                    parent[email] = account[1]
                email_to_name[email] = account[0]
                union(account[1], email)

        groups = collections.defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)
        
        return [[email_to_name[root]] + sorted(emails) for root, emails in groups.items()]
        
