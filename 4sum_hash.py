class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length<4:
            return []
            
        result = []
        dic = dict()
        for x in range(length-1):
            for y in range(x+1,length):
                if nums[x]+nums[y] not in dic: 
                    dic[nums[x]+nums[y]] = [{x,y}]
                else:
                    dic[nums[x]+nums[y]].append({x,y})
                    
        for s in dic:
            if target-s not in dic:
                continue
            
            for set1 in dic[s]:
                for set2 in dic[target-s]:
                    if set1.intersection(set2)==set():
                        indexs = map( lambda t:nums[t],list(set1)+list(set2))
                        list.sort(indexs)
                        result.append(indexs)
        nondup = []
        for li in result:
            if li not in nondup:
                nondup.append(li)
        return nondup        
