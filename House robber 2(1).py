nums = [int(x) for x in input("Enter values :").split(" ")]

'''
First Approach : Either Start from House One or Start from House 2
 For Implementation we are using Dynamic Approach
 Again House are in Circular Means, First and last House are Adjacent
Input: [1,100,2,1,1,1,100,1]

    Start from First House = [1,100,3]
    max(max(nums[x-3],nums[x-2]) + nums[x]),nums[x-1])
    [1,100,3,3,101,101,]
    [0,1,2,3,4,5,6,7,8]
'''
if(len(nums) <= 3):
    print(max(nums))
def startfromone():
    dp = [0]*(len(nums)-1)
    dp[0] = nums[0]
    dp[1] = nums[1]
    dp[2] = nums[0] + nums[2]
    for x in range(3,len(nums)-1):
        dp[x] = max(max(dp[x-3],dp[x-2]) + nums[x],dp[x-1])
    print(dp)
    return dp[-1]
def startfromtwo():
    dp = [0]*(len(nums))
    dp[0] = 0
    dp[1] = nums[1]
    dp[2] = nums[2]
    for x in range(3,len(nums)):
        dp[x] = max(max(dp[x-3],dp[x-2]) + nums[x],dp[x-1])
    print(dp)
    return dp[-1]

print(max(startfromone(),startfromtwo()))

