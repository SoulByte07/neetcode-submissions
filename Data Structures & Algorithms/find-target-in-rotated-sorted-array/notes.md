Common Pitfalls
Using Strict Inequality When Comparing with Left Element
In the one-pass binary search, the condition nums[l] <= nums[mid] uses <= rather than <. This handles the edge case when l == mid, which occurs in small subarrays. Using < instead can cause incorrect half selection and miss the target.

Confusing Pivot Finding with Target Finding
The two-pass approach requires finding the pivot first (smallest element), then searching the appropriate half. Do not conflate these steps. The pivot search uses nums[mid] > nums[r] to move left, while the target search is a standard binary search. Mixing the logic leads to wrong results.

Not Handling the Non-Rotated Array Case
When the array is not rotated (or rotated by 0), the pivot is at index 0. Your solution should still work correctly. Test with sorted arrays like [1, 2, 3, 4, 5] to ensure your pivot-finding logic returns index 0 and the subsequent search works.
