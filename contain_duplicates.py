#!/usr/bin/env python
# encoding: utf-8

# Method1 find max and min and do the check like bucket
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<1:
            return False
        max = nums[0]
        min = nums[0]
        #find the max and min in O(1.5n)
        mins = list()
        maxs = list()
        i=0
        while i<len(nums):
            if i==len(nums)-1:
                mins.append(nums[i])
                maxs.append(nums[i])
                break
            elif nums[i]<nums[i+1]:
                mins.append(nums[i])
                maxs.append(nums[i+1])
                i += 2
            else:
                mins.append(nums[i+1])
                maxs.append(nums[i])
                i += 2
        for k in mins:
            if min > k:
                min = k
        for p in maxs:
            if max < p:
                max = p

        bucket = [0]*int(max-min+1)
        for num in nums:
            bucket[num-min] +=1
        for times in bucket:
            if times > 1:
                return True
        return False


#Method 2
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<1:
            return False
        max = nums[0]
        min = nums[0]
        #find the max and min in O(1.5n)
        for num in nums:
            if num >= max:
                max = num
            if num < min:
                min = num


        bucket = [0]*int(max-min+1)
        for num in nums:
            if bucket[num-min] >0:
                return True
            bucket[num-min] +=1

        return False

#Method 3 to sort first
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True

        return False

