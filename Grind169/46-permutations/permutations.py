class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if n == len(sol):
                ans.append(sol[:])
                return
            
            for x in nums:
                if x in sol:
                    continue
                
                sol.append(x)
                backtrack()
                sol.pop()
        
        backtrack()
        return ans
        
        # Time Complexity: O(n!)
        # Space Complexity: O(n)