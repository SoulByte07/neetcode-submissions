while (i + length) in num_set:

A number is the start of a sequence if num - 1 is not in the set.
This guarantees that each consecutive sequence is counted exactly once.

Once we identify such a starting number, we simply keep checking if num + 1, num + 2, … exist in the set and extend the streak as far as possible.

O(n): doesnt have to be use single loop
