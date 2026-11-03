class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = nums.count(0)
        
        if zeros>1:
            return [0]*len(nums)
        
        product=1
        for i in range(len(nums)):
            if nums[i]!=0:
                product*=nums[i]
                
        if zeros==1:
            return [product if nums[i]==0 else 0 for i in range(len(nums))]
        print(product,'product')
        return [product//nums[i] for i in range(len(nums))]