'''
Problem: Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that
         each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        count_sum = {}
        for index, n in enumerate(nums):
            first = n
            second = target - n

            if second in count_sum.keys():
                return [count_sum[second], index]
            
            count_sum[first] = index

if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9

    s = Solution()
    print(s.twoSum(arr, target))