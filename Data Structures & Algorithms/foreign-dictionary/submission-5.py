class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word} # bug 1
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    graph[c2].add(c1)
                    break # bug 2

        state = {}
        order = []

        def dfs(c):
            if c in state:
                return state[c] == 2 # 2→跳过，1→有环

            state[c] = 1

            for pre in graph[c]:
                if not dfs(pre):
                    return False
            
            state[c] = 2
            order.append(c)
            return True # bug 3

        for c in graph:
            if not dfs(c):
                return ""
        return "".join(order)
        
        