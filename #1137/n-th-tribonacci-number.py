class Solution:
    def tribonacci(self, n: int) -> int:
        _temp = {}
        _temp[0] = 0
        _temp[1] = 1
        _temp[2] = 1
        i = 3
        while True:

            _temp[i] = _temp[i - 3] + _temp[i - 2] + _temp[i - 1]
            if i >= n:
                break
            i += 1

        return _temp[n]