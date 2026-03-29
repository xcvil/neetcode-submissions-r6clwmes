class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self.tm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:

        flow = self.tm[key]

        l, r = 0, len(flow)

        while l < r: # choose [l, r) -> r can jump to m due to the exclusion
            m = l + (r-l)//2

            if flow[m][0] > timestamp:
                r = m
            else: # flow[m][0] <= timestamp, might be the answer, l need to converge to l == r
                l = m + 1
        return flow[l-1][1] if l > 0 else ""
        
