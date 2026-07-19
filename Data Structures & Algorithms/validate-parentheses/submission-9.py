class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        stack = []
        close = [')','}',']']
        pairs = ['()','{}','[]']

        for c in s:
            if c in close:
                if len(stack) == 0:
                    return False

                top = stack.pop()
                if not top + c in pairs:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

