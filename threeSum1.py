Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets

For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)


'''
Be careful about
1. I could remove the duplicates at the beginning, or at the end. But the latter is faster.
2. Different from twoSum, finish the loop to find all possible combinations.

Here are two of my solutions below:

'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        result = []    
        list.sort(nums)
        
        for x in range(len(nums)-2):
            target = -nums[x]
            if x>0 and target == -nums[x-1]:
                continue 
            i = x+1
            j = len(nums)-1
            while(i<j):
                if nums[i]+nums[j]<target:
                    i = i+1
                elif nums[i]+nums[j]>target:
                    j = j-1
                else:
                    while i<j and nums[i]==nums[i+1]:
                        i =i+1
                    while i<j and nums[j]==nums[j-1]:    
                        j =j-1
                    result.append([nums[x],nums[i],nums[j]])    
                    i=i+1
                    j=j-1
                    continue

        return result


        
