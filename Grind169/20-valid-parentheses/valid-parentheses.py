class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")": "(", "}": "{", "]": "["}

        stack = []
        for ch in s:
            if ch not in close_to_open:
                stack.append(ch)
                continue
            if not stack or stack[-1] != close_to_open[ch]:
                return False

            stack.pop()

        return not stack
