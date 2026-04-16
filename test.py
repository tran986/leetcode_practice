# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
nums = [2,7,11]
target = 18

id=1
for i in range(len(nums)): #index of 1st num
    for j in range(i + 1): #index of 2nd num
       if nums[i] + nums[j] == target:
           print([i, j])

# Given an integer x, return true if x is a palindrome, and false otherwise.
x = -121
if x < 0:
    print("False")
else:
    digit = [int(d) for d in str(abs(x))]
    digit_rev = digit[::-1]
    if digit == digit_rev :
        print("True")
    else:
        print("False")


#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
# and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#342 + 465

in1=[2,4,3]
in2=[5,6,4]

in1_r=in1[::-1]
in2_r=in2[::-1]

in1_map=int("".join(map(str, in1_r)))
in2_map=int("".join(map(str, in2_r)))
result=in1_map + in2_map
print([int(d) for d in reversed(str(result))])
"""

#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".
#Example 1:
#Input: strs = ["flower","flow","flight"]
#Output: "fl"
#Example 2:
#Input: strs = ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.

strs = ["flower","flow","flight"]
min_len = min(len(word) for word in strs)
prefix = ""

for i in range(min_len):
    char = strs[0][i]
    for word in strs:
        if word[i] != char:
            print(prefix)   # prints "fl" then exits
            break
    else:
        prefix += char      # only adds char if no mismatch

print(prefix)
        


    
    
        

"""
res = []
for w in word:
    chars = []
    for char in w:
        chars.append(char)
    res.append(chars)

for i in res:
    print(i)
print(i[0])
"""
