class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        freqs = sorted(count.values())

        unique = freqs[0]
        for freq in freqs[1:]:
            if freq == unique:
                return False
            unique = freq

        return True


        