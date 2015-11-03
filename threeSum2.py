#this is another way to solve threeSum which is slower.
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
        
        prev = None
        for x in range(len(nums)-2):
            target = -nums[x]
            if target == prev:
                continue 
            prev = target
            rs = self.twoSum(nums[x+1:],target)
            for r in rs:
                result.append([nums[x]]+r)

        return result
        
            
    def twoSum(self,nums,target):
        i = 0
        j = len(nums)-1
        tmprs = []
        tmpset = set()
        while(i<j):
            if nums[i]+nums[j]<target:
                i = i+1
            elif nums[i]+nums[j]>target:
                j = j-1
            else:
                if tuple([nums[i],nums[j]]) not in tmpset: 
                    tmprs.append( [nums[i],nums[j]])
                    tmpset.add(tuple([nums[i],nums[j]]))
                i=i+1
                j=j-1
                continue
        return tmprs        
