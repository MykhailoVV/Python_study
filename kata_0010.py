"""
The maximum sum subarray problem consists in finding the maximum sum of a
contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum
sum is the sum of the whole array. If the list is made up of only negative
numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list
or array is also a valid sublist/subarray.
"""


def max_sequence(arr):
    max_sum = summ = start = end = 0
    for pos in range(len(arr)):
        end += 1
        if summ < 0:
            start = pos
            end = pos + 1
        summ = sum(arr[start:end])
        if max_sum < summ:
            max_sum = summ
    return max_sum


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([-2, -3, -4, -1, -5]))
print(max_sequence([]))
