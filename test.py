# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

nums = [2,7,11]
target = 18

id=1
for i in range(len(nums)): #index of 1st num
    for j in range(i + 1): #index of 2nd num
       if nums[i] + nums[j] == target:
           print([i, j])

# Given an integer x, return true if x is a palindrome, and false otherwise.
x = -12345
digit = [int(d) for d in str(abs(x))]
digit_rev = digit[::-1]
if digit == digit_rev :
    print("True")
else:
    print("False")


     