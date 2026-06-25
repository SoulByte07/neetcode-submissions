Common Pitfalls
Comparing Mid with Left Instead of Right
In the lower bound approach, comparing nums[mid] with nums[left] instead of nums[right] can lead to incorrect boundary updates, especially when the array is not rotated or rotated by n positions. Comparing with the rightmost element consistently determines which half contains the minimum.

Off-by-One Errors in Boundary Updates
When nums[mid] < nums[right], the minimum could be at mid itself, so set right = mid (not mid - 1). When nums[mid] >= nums[right], the minimum must be in the right half, so set left = mid + 1. Using wrong update logic either skips the minimum or causes infinite loops.

Not Handling the Non-Rotated Case
A sorted array with no rotation (or rotated by n positions) is still valid input. The minimum is simply the first element. Some binary search implementations fail on this edge case by not recognizing that the entire array is already sorted. Always check if nums[left] < nums[right] to detect this case early.

