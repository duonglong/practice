def find_max_crossing_sub_array(A, low, high, mid):
    left_sum = None
    total_sum = 0
    max_left = None
    for i in range(low, mid + 1):
        total_sum += A[i]
        if not left_sum or total_sum > left_sum:
            left_sum = total_sum
            max_left = i

    right_sum = None
    total_sum = 0
    max_right = None
    for i in range(mid + 1, high + 1):
        total_sum += A[i]
        if not right_sum or total_sum > right_sum:
            right_sum = total_sum
            max_right = i
    return (max_left, max_right, left_sum + right_sum)

def find_max_sub_array(A, low, high):
    if low == high:
        return (low, high, A[low])
    mid = (low + high) // 2
    left_low, left_high, left_sum = find_max_sub_array(A, low, mid)
    right_low, right_high, right_sum = find_max_sub_array(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_sub_array(A, low, high, mid)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return (left_low, left_high, left_sum)
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return (right_low, right_high, right_sum)
    elif cross_sum >= left_sum and cross_sum >= right_sum:
        return (cross_low, cross_low, cross_sum)

def find_max_sub_array_brute_force(A):
    max_sum = None
    arr_len = len(A) - 1
    max_at = None
    for i in range(arr_len):
        max_per_range = 0
        for j in range(i+1, arr_len):
            max_per_range += A[j]
            if not max_sum or max_per_range > max_sum:
                max_sum = max_per_range
                max_at = j
    return max_at, max_sum

def find_max_sub_array_linear(A):
    max_so_far = None
    max_ending_here = 0
    for x in A:
        max_ending_here += x
        if not max_so_far or max_ending_here > max_so_far:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

# Stolen from geekforgeek
from sys import maxint
def maxSubArraySum(a, size):
 
    max_so_far = -maxint - 1
    max_ending_here = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

#A = [13, -3, -25, 20 -3, -16, -23, 18, 20 -7, 12, -5, -22, 15, -4, 7]
A = [-3, -1, -5]
print find_max_sub_array(A, 0, len(A) - 1)
print find_max_sub_array_brute_force(A)
print find_max_sub_array_linear(A)
print maxSubArraySum(A, len(A))
