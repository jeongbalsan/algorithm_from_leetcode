import re
import sys
import collections
from dataclasses import dataclass


@dataclass
class valid_palindrome:

    def palindrom_1(self, msg: str) -> bool:

        strs = [char.lower() for char in msg if char.isalnum()]

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

    def palindrom_2(self, msg: str) -> bool:

        strs: Deque = collections.deque([char.lower() for char in msg if char.isalnum()])


        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

    def palinrom_3(self, msg: str) -> bool:
        msg = msg.lower()
        msg = re.sub('[^0-9a-z]', '', msg)
        return msg == msg[::-1]


if __name__ == "__main__":
    msg = input()

    v = valid_palindrome()
    #print(v.palindrom_1(msg))
    #print(v.palindrom_2(msg))
    print(v.palinrom_3(msg))