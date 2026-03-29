class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pattern = collections.defaultdict(list)

        for i in range(len(beginWord)):
            p = beginWord[:i] + "*" + beginWord[i+1:]
            pattern[p].append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + "*" + word[i+1:]
                pattern[p].append(word)

        
        q = collections.deque()
        q.append(beginWord)
        dist = 0
        visited = set()
        visited.add(beginWord)

        while q:
            for _ in range(len(q)):
                currWord = q.popleft()
                if currWord == endWord:
                    return dist + 1
                for i in range(len(currWord)):
                    p = currWord[:i] + "*" + currWord[i+1:]
                    for nei in pattern[p]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            dist += 1
        return 0
            

