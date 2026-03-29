class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import operator
        cal = []
        ops = {
            '+' : operator.add,
            '-' : operator.sub,
            '*' : operator.mul,
            '/' : operator.truediv,
        }
        for t in tokens:
            if t not in ops:
                cal.append(int(t))
            else:
                val_r = cal.pop()
                
                val_l = cal.pop()
                
                val = int(ops[t](val_l, val_r))
                cal.append(val)

        return cal.pop()