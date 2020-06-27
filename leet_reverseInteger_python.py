"""
class Solution:
    def reverse(self, x: int) -> int:
 """

def temp(x):
    if x >= (-(2**31)) and x <= ((2**31)-1):
        x_str = str(x)
        # 0이 여러개일 수 있음. 30, 300, 3000 모두 결과값은 3 나와야됨.
        if x_str[:-1] == '0':
            x_str = x_str.pop(-1)
            print(x_str)



temp(300)