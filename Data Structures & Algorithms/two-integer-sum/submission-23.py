class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for i in range(len(nums)):
            look = target - nums[i]
            if look in my_dict and my_dict[look] != i:
                return [i, my_dict[look]]
             
        

            