Common Pitfalls
Not Taking the Maximum When Jumping the Left Pointer
In the optimal sliding window approach, when you find a duplicate character, you should move the left pointer to max(left, lastIndex[char] + 1). Forgetting the max operation can cause the left pointer to move backwards if the duplicate character's last occurrence is before the current window start, leading to incorrect results.

Forgetting to Update the Character's Last Index
After processing each character, you must update its last seen index in the map, regardless of whether it was a duplicate. Failing to update the index means future duplicate checks will reference stale positions, causing incorrect window calculations.

Off-by-One in Window Size Calculation
When calculating the substring length, ensure you use right - left + 1 since both indices are inclusive. Using right - left will undercount the length by one, resulting in an answer that is consistently one less than correct.
