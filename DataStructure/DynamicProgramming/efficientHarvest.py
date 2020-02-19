'''
Problem: A farmer uses pivot irrigation to water a circular field of crops. Due to varying conditions, the field does not produce 
         consistently. The farmer wants to achieve maximum profit using limited resources for harvest. The field is segmented into
         a number of sefments, and a profit us calculated for each segment. The profit is the cost to harvest versus the sale price
         of the produce. The farmer will harvest a number of contiguous segments along with those opposite. Determine the maximum
         profit the farmer can achieve.
         For example, the field is divided into n = 6 sections and will select k = 2 contiguous sections and those opposite to harvest.
         
'''
def maxProfit(k, field):
    pivot_pies = list()
    field_size = len(field)
    # Create an array with the sums of the opposite pies
    # Iterate from index zero to halfways and add the opposite pies to it
    for i in range(field_size// 2):
        print(i)
        opp_index = (field_size // 2) + i 
        pivot_pies.append(field[i] + field[opp_index])

    # print(pivot_pies)
    # Create a circular array
    pivot_pies = pivot_pies + pivot_pies[0:(k-1)]
    print(pivot_pies)

    # Select 'k' pivots and get the max profit
    max_profit, i = -999999, 0

    while i < len(pivot_pies)-(k-1):
        print(pivot_pies[i:i+k])
        temp = sum(pivot_pies[i:i+k])
        # print("Temp Profit:", temp)
        if max_profit < temp: max_profit = temp
        # print("max profit:",max_profit)
        i += 1

    return max_profit
   
'''
# Not Efficient Solution
def maxProfit(k, field):
    # return variable
    max_profit = -999999999

    # size to take slice of array
    n = len(field)

    # implement circular array
    cicr_field = field * 2

    for i in range(len(cicr_field)):
        # Take a slice from that index to the size of the array
        current_arr = cicr_field[i:i+n]
        print("Current Array:", current_arr)

        # If the current array is not of size n then break
        if len(current_arr) < n:
            break

        # Iterate in the current array an select the pie accordingly
        # We have to select opposite slices of the field
        current_profit = 0
        cntr = 0
        i = 0
        while cntr != k:
            # select a pie of the field
            print("Current index:", i)
            current_profit += current_arr[i]
            cntr += 1
            print("Counter:", cntr)

            # select the opposite pie
            opposite_index = (n // 2) + i
            print("Opposite index:", opposite_index)
            current_profit += current_arr[opposite_index]
            i += 1
        
        print("Current Profit:", current_profit)
        print("Max Profit:", max_profit)

        # if the current profit exceeds the max profit, replace
        if current_profit > max_profit: max_profit = current_profit

    return max_profit 
'''

if __name__ == "__main__":
    field = [1,5,1,-3,7,3]
    k = 2

    print(maxProfit(k, field))
