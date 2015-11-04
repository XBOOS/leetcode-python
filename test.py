nums = [0,0,0,0]
length = len(nums)
dic = dict()
for x in range(length-1):
    for y in range(x+1,length):
        if nums[x]+nums[y] not in dic: 
            dic[nums[x]+nums[y]] = [{x,y}]
        else:
            dic[nums[x]+nums[y]].append({x,y})


print dic
result = []
for sum in dic:
    if 0-sum not in dic:
        continue
    for set1 in dic[sum]:
        for set2 in dic[-sum]:
            if set1.intersection(set2)==set():
                print list.sort(map(lambda t:t+1,list(set1)+list(set2)))
                result.append(list.sort(map(lambda t:t+1,list(set1)+list(set2))))

print result
