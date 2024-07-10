class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = Counter()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i
        
        return [-1, -1]
        