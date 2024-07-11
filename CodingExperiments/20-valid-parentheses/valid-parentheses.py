class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for ch in s:
            if ch in list(hashmap.values()):
                stack.append(ch)
                continue
            if not stack or stack[-1] != hashmap[ch]:
                return False
            stack.pop()

        return not stack
        