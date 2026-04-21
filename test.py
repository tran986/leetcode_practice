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


#Input: n = 19
#Output: true
#Explanation:
#1^2 + 9^2 = 82
#8^2 + 2^2 = 68
#6^2 + 8^2 = 100
#1^2 + 0^2 + 0^2 = 1 -> happy number, return true

n=13
seen = set()
while n != 1:
    if n in seen:
        print(False)
        break
    seen.add(n)
    digit_sum = []
    for digit in str(n):
        square = int(digit) ** 2
        digit_sum.append(square)
    n = sum(digit_sum)

print(True)
"""
"""
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""
rom_num = "XIX" #return 11

symbol = {"I":1,
          "V":5,
          "X":10,
          "L":50,
          "C":100,
          "D":500,
          "M":1000}
total = 0
for i in range(len(rom_num) - 1):
    current_num = symbol[rom_num[i]]
    next_num = symbol[rom_num[i + 1]]
    if current_num < next_num :
        total -= current_num
    else:
        total += current_num
total += symbol[rom_num[-1]]
print(total)

