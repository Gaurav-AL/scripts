nums = [int(x) for x in input("Enter the Array :").split(" ")]
for x in range(1,len(nums)):
    if(nums[x-1] >0):
        nums[x] = nums[x] + nums[x-1]
print(max(nums))
