<h2>convert-an-array-into-a-2d-array-with-conditions Notes</h2><hr>Complexity Analysis

Here, NNN is the size of array nums.

Time complexity: O(N)O(N)O(N)

We iterate over the array nums once to insert them into the 2D array ans. Accessing freq and incrementing it takes O(1)O(1)O(1). Hence, the total time complexity is equal to O(N)O(N)O(N).

Space complexity: O(N)O(N)O(N)

The size of the frequency array freq is equal to nums.size() + 1 as the value of integers in the array nums can be up to nums.size(). Hence, the total space complexity is equal to O(N)O(N)O(N).