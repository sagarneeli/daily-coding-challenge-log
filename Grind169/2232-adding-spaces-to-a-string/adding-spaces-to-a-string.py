class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        words = []
        start = 0

        for end in spaces:
            word = s[start: end]
            words.append(word)
            start = end
        
        if end < len(s):
            end_word = s[end: len(s)]
            words.append(end_word)

        return " ".join(words)

        