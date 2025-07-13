class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are not palindromes
        # Also, numbers ending in 0 cannot be palindromes unless the number is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # For even digit numbers: x == reversed_half
        # For odd digit numbers: x == reversed_half // 10 (middle digit doesn't matter)
        return x == reversed_half or x == reversed_half // 10
