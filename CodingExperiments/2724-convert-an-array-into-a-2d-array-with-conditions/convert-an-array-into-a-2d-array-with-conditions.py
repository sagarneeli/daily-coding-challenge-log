class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = defaultdict(int)
        result = []

        for num in nums:
            current_row = count[num]
            if len(result) == current_row:
                result.append([])
            
            result[current_row].append(num)
            count[num] += 1
        
        return result
        