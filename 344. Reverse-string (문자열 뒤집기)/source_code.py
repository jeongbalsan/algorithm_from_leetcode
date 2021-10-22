from dataclasses import dataclass


@ dataclass
class Solution:

    def reverseString_self(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        print(s)
        s = [i for i in s[::-1]]
        print(s)

    def reverseString_1(self, s: list[str]) -> None:
        print(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        print(s)

    def reverseString_2(self, s: list[str]) -> None:

        print(s)

        s.reverse()

        print(s)

    def reverseString_self_tip(self, s: list[str]) -> None:

        print(s)
        
        # s = s[::-1]
        s[:] = s[::-1]

        print(s)


s = ["H","a","n","n","a","h"]
u = Solution()
#u.reverseString_self(s)
u.reverseString_2(s)
