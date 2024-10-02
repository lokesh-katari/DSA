Kadane’s Algorithm is an efficient algorithm used to find the maximum sum of a contiguous subarray in an array of integers (both positive and negative). It operates with a time complexity of O(n), where n is the number of elements in the array.

Core Idea:
The algorithm maintains a running sum of the current subarray, updating it as it iterates over the array. It keeps track of two things:

Current Sum (current_sum): Sum of the current subarray.
Maximum Sum (max_sum): Maximum sum found so far.
At each step, Kadane’s Algorithm checks:

If adding the current element to the current_sum increases the sum, keep it.
Otherwise, restart the subarray from the current element, effectively resetting the current_sum.
Steps:
Initialize current_sum and max_sum to the first element of the array.
Iterate over the array starting from the second element.
For each element, update the current_sum by taking the maximum of the current element and current_sum + current element.
Update max_sum if current_sum is greater than max_sum.
Return max_sum at the end, which will be the maximum sum of a contiguous subarray.

Key Points:
Time Complexity: O(n) because we traverse the array only once.
Space Complexity: O(1) because we are using a constant amount of space for the variables current_sum and max_sum.
