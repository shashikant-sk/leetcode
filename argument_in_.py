# Argument in python are passed by value or by reference?
# ans :-  pytho aregument passed my the the referrance so any change made within a fuction is reflected on the original object passed as an argument.


# def func(a):
#     l[0] = 3

# l = [1, 2, 3, 4]

# func(1)  # Fixed the typo in the function call

# print(l)



# =====================
def fuc(l):
    l=[1,2,3,4]
l=[1,2,3,4]
fuc(l)
print(l)