# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#         res=0 # result variable for what we will return at the end of the function 
#         for i in range(len(s)): # loop through the string
#             if i+1<len(s) and roman[s[i]] < roman[s[i+1]]: # if the current roman numeral is less than the next roman numeral how its working? = IX = 1<10 = True
#                 res -=roman[s[i]] # subtract the current roman numeral from the result variable how its working? = 0-1 = -1
#             else:
#                 res+=roman[s[i]] # add the current roman numeral to the result variable how its working? = -1+10 = 9
#         return res # return the result variable how its working? = 9



# ---------------------------------------------------------------

class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a dictionary to map Roman numerals to their corresponding values.
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        res = 0  # Initialize the result to 0, where the final integer value will be stored.
        
        # Iterate through each character in the input Roman numeral string.
        for i in range(len(s)):
            # Check if the next character has a greater value than the current one.
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                # If so, subtract the current value from the result (as it's a subtraction case).
                res -= roman[s[i]]
            else:
                # If not, add the current value to the result.
                res += roman[s[i]]
        
        return res  # Return the calculated integer value.
