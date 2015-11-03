# remove duplicated items in sorted list and return the new length
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        length = len(nums)
        if length<2:
            return length
        while i<length:
            while i>0 and i<length and nums[i]==nums[i-1]:
                nums.pop(i)
                length-=1
            i+=1
            continue
        return length
