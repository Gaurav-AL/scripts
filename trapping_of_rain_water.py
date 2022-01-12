nums = [int(x) for x in input("Enter the Block Heights :").split(" ")]
max_left,max_right,trapped_water = [nums[0]],[nums[len(nums)-1]],0

for x in range(1,len(nums)):
    max_left.append(max(max_left[x-1],nums[x]))

for x in reversed(range(len(nums))):
    
    max_right.append(max(max_right[len(nums)-x-1],nums[x-1]))
    
print(max_left,max_right)
for x in range(1,len(nums)-1):
    trapped_water += min(max_left[x-1],max_right[x+1]) - nums[x]) 
print(trapped_water)
