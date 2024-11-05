class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")
        prev_word = words[0]
        last_word = words[-1]
        
        if prev_word[0] != last_word[-1]:
            return False

        for next_word in words[1:]:
            if prev_word[-1] != next_word[0]:
                return False
            else:
                prev_word = next_word
        
        return True

        