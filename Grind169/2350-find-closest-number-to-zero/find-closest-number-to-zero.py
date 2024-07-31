class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_num = nums[0]

        for n in nums:
            if abs(n) < abs(closest_num):
                closest_num = n
        
        if closest_num < 0 and abs(closest_num) in nums:
            return abs(closest_num)
        
        return closest_num

        # Time - O(N)
        # Space - O(1)
        


        