class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==1:
            return 1   
        speed = [s for _, s in sorted(zip(position, speed))]
        position.sort()
        stack = []
        # monotonic increasing?
        for p, s in zip(position, speed):
            curr_t = (target-p)/s
            while stack and curr_t >= stack[-1]:
                stack.pop()
            stack.append(curr_t)

        return len(stack)
