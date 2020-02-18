'''
Problem: HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent
         by a client on a particular day is greater than or equal to 2x the client's median spending for a trailing number of days, they
         send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least
         that trailing number of prior days' transaction data.
         Given the number of trailing days d and a client's total daily expenditures for a period of n days, find and print the number of
         times the client will receive a notification over all n days.
         For example, d = 3 and expenditures = [10, 20, 30, 40, 50]. On the first three days, they just collect spending data. At day 4, 
         we have trailing expenditures of [10, 20, 30]. The median is 20 and the day's expenditure is 40. Because 40 >= 2 * 20, there will
         be a notice. The next day, our trailing expenditures are [20, 30, 40] and the expenditures are 50. This is less than 2 * 30 so no
         notice will be sent. Over the period, there was one notice sent.
         Note: The median of a list of numbers can be found by arranging all the numbers from smallest to greatest. If there is an odd 
         number of numbers, the middle one is picked. If there is an even number of numbers, median is then defined to be the average of the
         two middle values. (Wikipedia)

    Function Description: Complete the function activityNotifications in the editor below. It must return an integer representing the number
         of client notifications.
         activityNotifications has the following parameter(s):
            --> expenditure: an array of integers representing daily expenditures
            --> d: an integer, the lookback days for median spending

    Input Format: The first line contains two space-separated integers n and d, the number of days of transaction data, and the number of
        trailing days' data used to calculate median spending.
        The second line contains n space-separated non-negative integers where each integer i denotes expenditure[i].

    Constraints:    1 <= n <= 2 * 10^5
                    1 <= d <= n
                    0 <= expenditure[i] <= 200

    Output Format: Print an integer denoting the total number of times the client receives a notification over a period of n days.
'''
# High time complexity
'''
def activityNotifications(arr, d):
    notification = 0

    for i in range(len(arr) - d):
        # Slice of the transaction
        t_window = sorted(arr[i:(i+d)])

        # get median of t-window
        if d % 2 != 0:
            # If array size (n) is odd then the median is the index at (n - 1) / 2
            median = t_window[(d - 1) // 2]
        else:
            # If array size is even then median is the avg. of the central 2 numbers
            median = (t_window[(d - 1) // 2] + t_window[d // 2]) / 2
    
        if arr[i+d] >= (2 * median):
            notification += 1 
        else: continue

    return notification
'''

import bisect

def activityNotifications(arr, d):
    # if the size of arr is less than d, return 0
    if len(arr) < d : return 0

    # initialize
    notification = 0
    midpoint = d // 2
    is_even = d % 2 == 0

    # Initial array
    ex_window = sorted(arr[:d])
    # print(ex_window)

    for i, current_expense in enumerate(arr[d:]):
        # Calculate the median
        if is_even:
            median = ex_window[midpoint - 1] + ex_window[midpoint]
        else:
            median = 2 * ex_window[midpoint]

        # print(median)

        # Check for notification
        if current_expense >= median: notification += 1

        # Shift the window
        ## locate the index of the first element in ex_window
        index_to_remove = bisect.bisect_left(ex_window, arr[i])
        del ex_window[index_to_remove]

        # print("After delete:", ex_window)

        # insert the new value
        bisect.insort(ex_window, current_expense)
        # print("After insert:", ex_window)
    
    return notification


if __name__ == "__main__":
    #num_days, days_bracket = map(int, input().split())
    #expenditure = list(map(int, input().split()))

    days_bracket = 3
    expenditure = [10,20,30,40,50]

    '''
    with open('input.txt') as in_f:
        num_days, days_bracket = map(int, in_f.readline().split())
        expenditure = list(map(int, in_f.readline().split()))
    '''

    print(activityNotifications(expenditure, days_bracket))