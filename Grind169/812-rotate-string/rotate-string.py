class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        i, n = 0, len(s)
        """
        abcde
        bcdea
        cdeab
        """
        while i < n:
            left_most_ch = s[0]
            new_str = s[1:] + left_most_ch
            print(new_str)
            if new_str == goal:
                return True
            s = new_str
            i = i + 1

        return False
            
        