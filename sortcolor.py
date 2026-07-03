class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)

        for i in range(n):
            for j in range(n-2,-1,-1):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j]=nums[j+1]
                    nums[j+1]=temp
