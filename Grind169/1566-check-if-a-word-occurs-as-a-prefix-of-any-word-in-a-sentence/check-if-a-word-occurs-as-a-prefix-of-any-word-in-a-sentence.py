class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        def is_prefix(current_word, search_word):
            n = len(search_word)
            if len(current_word) < n:
                return False
            
            if current_word[:n] == search_word:
                return True
            
            return False

        mapper = {}
        for i, ch in enumerate(sentence.split(" ")):
            if i + 1 in mapper:
                continue
            mapper[i + 1] = ch

        print(mapper)
        for k, v in mapper.items():
            if is_prefix(v, searchWord):
                return k

        return -1

        