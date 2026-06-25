Common Pitfalls
Not Updating maxf Correctly
The variable maxf tracks the highest frequency seen while expanding the window, not necessarily the exact maximum frequency after every shrink. A common mistake is recalculating the maximum by iterating through all counts after moving the left pointer. In the optimal solution, you do not need to decrease maxf when shrinking. A stale, higher maxf can temporarily make the validity check more permissive and allow an actually invalid current window, but it does not affect correctness because it cannot make the algorithm record a length larger than one that was achievable when maxf was accurate.

Shrinking the Window Too Aggressively
When the tracked condition is violated (window size - maxf > k), you only need to shrink until that condition passes again. A common error is resetting the left pointer too far or not updating character counts properly when moving the left pointer. Make sure to decrement the count of s[l] before incrementing l.

Confusing Window Size Calculation
The window size is r - l + 1, not r - l. This off-by-one error is frequent and leads to incorrect validity checks. For example, if l = 0 and r = 2, the window contains 3 characters, not 2. Always double-check your window size formula in the condition (r - l + 1) - maxf <= k.
