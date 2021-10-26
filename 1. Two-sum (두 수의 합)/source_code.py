
class Solution:

    def twoSum_self(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    def twoSum_1(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:

                return [nums.index(n), nums.index(complement, i+1)]


    def twoSum_2(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            nums_map[num] = i

        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]


    def twoSum_3(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]

            nums_map[num] = i




if __name__=='__main__':
    
    nums = [3,2,4]
    target = 6

    s_t = Solution()

    print(s_t.twoSum_3(nums, target))