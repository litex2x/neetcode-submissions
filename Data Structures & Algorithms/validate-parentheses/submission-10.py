class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        pairs = {')':'(','}':'{',']':'['}

        for c in s:
            if c in pairs:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if pairs[c] != top:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

