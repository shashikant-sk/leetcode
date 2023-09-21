# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x<0:
#             return False
#         div =1
#         while x>=div * 10:
#             div *=10
#         while x:
#             right = x%10
#             left = x//div
#             if left != right:
#                 return False
#             x = (x%div)//10 # remove the leftmost digit how its working? = 121%100 = 21//10 = 2
#             div //=100 # remove the rightmost digit how its working? = 121//100 = 1 leftmost digit removed
#         return True            

## return False if x < 0 else str(x)[::-1] == str(x)
