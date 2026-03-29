class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        words, dist = set(wordList), 0

        q = collections.deque()
        q.append(beginWord)

        while q:
            dist += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return dist
                
                for i in range(len(curr)):
                    for c in range(97, 123):
                        if chr(c) == curr[i]:
                            continue
                        nei = curr[:i]+chr(c)+curr[i+1:]

                        if nei in words:
                            q.append(nei)
                            words.remove(nei)

        return 0
