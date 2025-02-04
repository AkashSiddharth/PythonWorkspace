'''
Problem: Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
         Example 1:
            Input:  nums = [1,1,1], k = 2
            Output: 2
         Note:
            - The length of the array is in range [1, 20,000].
            - The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''
from collections import Counter

class Solution:
    def subarraySum(self, nums, k):
        count = Counter()
        count[0] = 1
        s = ans = 0
        for num in nums:
            s += num
            ans += count[s - k]
            count[s] += 1
        
        return ans

if __name__ == "__main__":
    arr = [-1,-1,1]
    target = 0

    s = Solution()
    print(s.subarraySum(arr, target))