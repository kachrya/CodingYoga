# given two sorted arrays, find the median
# expected time complexity is O(log n)
import math

A = [1, 3]# 5, 7, 9]
B = [1, 2]#, 4, 6, 8, 9, 10]


"""
Returns median index and median value.
For even sized array, returns index of the lesser of
the two middle values, and average of two middle values
"""


def find_median_of_array(A):
    if len(A) % 2 == 1:
        index = math.floor(len(A)/2)
        return index, A[index]
    else:
        index = math.floor(len(A)/2) - 1
        return index, (A[index] + A[index+1])/2


def find_median_of_two(A, B):
    median_index_1, median1 = find_median_of_array(A)
    median_index_2, median2 = find_median_of_array(B)
    while True:
        print("Median1 %r [%r] Median2 %r [%r]"
              % (median1, median_index_1, median2, median_index_2))
        if len(A) == 2 and len(B) == 2:
            break

        if median1 < median2:
            if len(A) != 2:
                A = A[median_index_1:]
            if len(B) != 2:
                B = B[:median_index_2+1]
        else:
            if len(A) != 2:
                A = A[:median_index_1+1]
            if len(B) != 2:
                B = B[median_index_2:]
        print("A = %r B = %r" % (A, B))
        median_index_1, median1 = find_median_of_array(A)
        median_index_2, median2 = find_median_of_array(B)
    median = (max(A[0], B[0]) + min(A[1], B[1])) / 2
    return median


#print(find_median_of_array(B))
#print(len(A))
print(find_median_of_two(A, B))
