class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        freqs = sorted(count.values())

        return len(freqs) == len(set(freqs))


        