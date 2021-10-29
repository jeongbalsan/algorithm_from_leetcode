class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum


    def arrayPairSum1(self, nums: list[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):

            if i % 2 == 0:

                sum += n

        return sum


    def arrayPairSum2(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])


if __name__ == "__main__":

    nums = [6,2,6,5,1,2]

    cs = Solution()

    print(cs.arrayPairSum2(nums))




