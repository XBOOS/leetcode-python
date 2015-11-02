'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''

'''
1. Be careful about the list deep copy
2. deuplicated numbers
3.index ordering : need backup before sorting


'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<2:
            return []
        backup = nums[:]    
        list.sort(nums)
        i = 0
        j = len(nums)-1
        while i<j:
            if (nums[i]+nums[j])<target:
                i=i+1
            elif (nums[i]+nums[j])>target: 
                j=j-1
            else:
                if nums[i]==nums[j]:
                    index1 = backup.index(nums[i])
                    backup.remove(nums[i])
                    return [index1+1,backup.index(nums[j])+2]    
                else:
                    index1 = backup.index(nums[i])+1
                    index2 = backup.index(nums[j])+1
                    return [min(index1,index2),max(index1,index2)]
           
