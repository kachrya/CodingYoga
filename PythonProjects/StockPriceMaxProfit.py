A = [530, 520, 510, 505, 540, 545, 516, 499, 501, 589, 429, 519]
#A = [10, 7, 5, 8, 11, 9]

#A = [500, 499, 498, 495, 493, 490]
#A = [498, 499, 500, 501, 502, 505 ]
def find_max_profit(A):
    lowest_price_so_far = A[0]
    max_profit = 0
    for i in range(1, len(A)):
        current_profit = A[i] - lowest_price_so_far
        if current_profit < 0:
            lowest_price_so_far = A[i]
        else:
            max_profit = max(current_profit, max_profit)
        print(A[i], current_profit, max_profit)

    return max_profit


print(find_max_profit(A))




