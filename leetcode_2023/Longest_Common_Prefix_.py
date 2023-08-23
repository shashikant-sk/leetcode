# # class class Solution:
# #     def longestCommonPrefix(self, strs: List[str]) -> str:
#         # if not strs:
#         #    return ''
    
#         # for i in range(len(strs[0])):
#         #     for j in range(1, len(strs)):
#         #         if i == len(strs[j]) or strs[j][i] != strs[0][i]:
#         #             return strs[0][:i]

#         # return strs[0]
        
# # ------------------------------------------------------------------------------------------------------------------------        
#         # result = '' # empty string
#         # for i in zip(*strs):  # for each character in the first string (zip(*strs) is a list of tuples)  zip is a function that takes iterables (can be zero or more), aggregates them in a tuple, and return it
#         #     if len(set(i)) == 1:
#         #         result += i[0]
#         #     else:
#         #         break
#         # return result

# # ------------------------------------------------------------------------------------------------------------------------
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         result = ''  # empty string
#         for i in range(len(strs[0])): # for each character in the first string
#             for j in strs: # for each string in the list
#                 if i == len(j) or j[i] != strs[0][i]: # if the character is not the same or the index is out of range
#                     return result # return the result
#             result += strs[0][i] # add the character to the result
#         return result # return the result
# # ------------------------------------------------------------------------------------------------------------------------

# Result = ''
# for i in zip(*strs):
#     if len(set(i))==1:
#         Result +=i[0]
#     else:
#         break
# return Result 

s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
result = list(zip(s1, s2))
print(result)
