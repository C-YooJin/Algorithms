class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif str(x)[::-1] == str(x):
            return True
        else:
            return False

print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(22))