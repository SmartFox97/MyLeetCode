# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:

    def getHalf(self) -> int:
        return int((self.min + self.max) / 2)

    def guessNumber(self, n: int) -> int:
        self.min = 1
        self.max = n
        _num = 0
        while True:
            _num = self.getHalf()
            if guess(_num) == -1:
                self.max = _num - 1
            elif guess(_num) == 1:
                self.min = _num + 1
            elif guess(_num) == 0:
                break
        return _num