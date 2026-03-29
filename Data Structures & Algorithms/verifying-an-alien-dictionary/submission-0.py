class Solution:
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                # w1 比 w2 长，且前缀完全相同 → 不合法
                if j >= len(w2):
                    return False
                # 找到第一个不同的字符
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break  # w1[j] < w2[j]，已确认有序，不用继续
        return True

