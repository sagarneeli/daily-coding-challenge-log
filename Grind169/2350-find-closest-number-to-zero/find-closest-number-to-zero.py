class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        dist_to_num = {}
        for n in nums:
            diff = abs(n) - 0
            if diff not in dist_to_num:
                dist_to_num[diff] = [n]
            else:
                dist_to_num[diff].append(n)
        
        closest_num = min(dist_to_num.keys())
        return max(dist_to_num[closest_num])
        


        