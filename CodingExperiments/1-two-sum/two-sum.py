class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_map = Counter()

        for i, num in enumerate(nums):
            if target - num in count_map:
                return [i, count_map[target-num]]
            count_map[num] = i
        
        return [-1, -1]
        