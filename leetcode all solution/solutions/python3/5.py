# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         def check(l, r): 
#             while 0 <= l <= r < len(s) and s[l] == s[r]: 
#                 l -= 1
#                 r += 1
#             return s[l + 1:r]
#         pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
#         return sorted(pals, key = len)[-1] if pals else ''
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l, r): 
            # This function checks for the longest palindrome substring centered at l and r.
            # It expands outwards from l and r and returns the palindrome substring found.
            while 0 <= l <= r < len(s) and s[l] == s[r]: 
                l -= 1
                r += 1
            return s[l + 1:r]
        
        # Create a list called 'pals' to store all palindrome substrings.
        # It generates palindrome substrings by checking both odd-length and even-length palindromes.
        pals = [check(i, i) for i in range(len(s))] + [check(i, i + 1) for i in range(len(s) - 1) if s[i] == s[i + 1]]
        
        # Return the longest palindrome substring from the 'pals' list using 'sorted' and 'key'.
        # The key for sorting is the length of the palindrome substring.
        # Return the longest palindrome substring, or an empty string if no palindromes are found.
        return sorted(pals, key=len)[-1] if pals else ''
