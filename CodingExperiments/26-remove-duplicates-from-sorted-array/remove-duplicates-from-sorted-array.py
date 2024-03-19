class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Pattern - Two-pointer approach
        Hint: Sorted array, in-place deletion

        Idea:
        1. Initialize a left, right pointers with starting position index = 1
        2. Left pointer tracks unique elements in the array
        3. Right pointer iterates through the array
        4. Whenever we encounter a new unique value we add the right pointer to left
        """
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        
        return l

        