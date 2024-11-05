class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        prev, fancy_string, freq = s[0], s[0], 1

        for i in range(1, len(s)):
            if s[i] == prev:
                freq += 1
            else:
                prev = s[i]
                freq = 1
            
            if freq < 3:
                fancy_string += s[i]

        return fancy_string


        