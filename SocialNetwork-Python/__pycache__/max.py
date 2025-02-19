def maxsum(nums):
    re=0
    for i in range(len(nums)):
        # for j in range (len(nums[i])):
        #     print(nums[i],nums[j])
        #     if i!=j :
        #             if nums[i]+nums[j]>re:
        #                 re=nums[i]+nums[j] 
        digitSum = 0
        while (nums > 0) :
            digitSum += num % 10
            num /= 10
        
    return re  
print(maxsum(eval(input())))