class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        n = len(s)
        for _ in range(n):
            s = s[1:] + s[0]
            if s == goal:
                return True

        return False
            
        