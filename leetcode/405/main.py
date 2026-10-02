class Solution:
    def toHex(self, num: int) -> str:
        """Представить 32-битное число в шестнадцатеричной системе."""
        if num == 0:
            return "0"

        digits = "0123456789abcdef"
        num &= 0xFFFFFFFF
        result = []

        while num:
            result.append(digits[num & 0xF])
            num >>= 4

        return "".join(reversed(result))
