def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        print("index = %r " % A.index(x))
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print("max_ending_here = %d max_so_far = %d " % (max_ending_here, max_so_far))
    return max_so_far


def max_subarray_index(A):
    max_ending_here = max_so_far = A[0]
    start_index = end_index = 0
    print(A)
    for i in range(1, len(A)):

        print("A[%d] = %d max_ending_here %d max_so_far %d start %d end %d "
              % (i, A[i], max_ending_here, max_so_far, start_index, end_index))
        if A[i] > (max_ending_here + A[i]):
            max_ending_here = A[i]
            start_index = i
        else:
            max_ending_here += A[i]
            end_index = i
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            max_so_far_start = start_index
            max_so_far_end = end_index

    return max_so_far, max_so_far_start, max_so_far_end


def max_subarray_index_less_k(A, k):
    max_ending_here = max_so_far = A[0]
    start_index = end_index = 0
    for i in range(1, len(A)):
        print(A)
        print("A[%d] = %d max_ending_here %d max_so_far %d start %d end %d "
              % (i, A[i], max_ending_here, max_so_far, start_index, end_index))
        if A[i] > (max_ending_here + A[i]) and A[i] <= k:
            max_ending_here = A[i]
            start_index = i
        elif A[i] <= (max_ending_here + A[i]) and (max_ending_here + A[i]) <= k:
            max_ending_here += A[i]
            end_index = i
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            max_so_far_start = start_index
            max_so_far_end = end_index
        if max_ending_here == k:
            break
    return max_so_far, max_so_far_start, max_so_far_end

A = [-2, -3, 4, -1, -2, 1, 5, -3]
#A = [-3, -2, -8, -1, -9]
#A = [-3, -2, 3, 3, 6, -2, -6, -4, 4, 8, 1, -1, 5]
#print("Max sum = %d start index = %d end index = %d" % max_subarray_index(A))

print("Max sum = %d start index = %d end index = %d" % max_subarray_index_less_k(A, 6))
#print("Max sum = %d" % max_subarray(A))