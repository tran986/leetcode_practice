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


Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

a = "11"
b = "1"
sum_str = int(a) + int(b)
print(bin(sum_str)[2:])

x = 121
for i in range(len(x)):
    print(x)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

#for i in range(len(nums) - 2):
#    a, b, c = nums[i], nums[i+1], nums[i+2]
    #print(nums[i] + nums[i+1] + nums[i+2])
"""
nums = [-1,0,1,2,-1,-4]
nums=sorted(nums, reverse = False)
print(nums)
result = []
for i in range(0, len(nums) - 2):
    left = i + 1
    right = len(nums) - 1
    while left < right and nums[left] == nums[left - 1]:
        if nums[i] + nums[right] + nums[left] == 0:
            print([])
            left += 1
        elif nums[i] + nums[right] + nums[left] < 0:
            left += 1
        else: 
            right -= 1
    result.append([nums[i], nums[left], nums[right]])

print(result)

#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.   
num = 10
while num >= 10:
    total = 0
    for d in str(num):
       digit = int(d)
       total += digit
    num = total #assign the new num as total before checking if they are >= 10
#print(num)

#Shortest Word Distance:
words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"

idx2 = words.index(word2)
idx1 = words.index(word1)
min_dist = float("inf")
#call index of word 1 is i, and index of word 2 is j
for i in range(len(words)):
    for j in range(len(words)):
        if words[i] == word1 and words[j] == word2:
            min_dist = min(min_dist, abs(i-j))

print(min_dist)

#Rosalind problems:
#1.using slice:
list = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
#print(list[0:6] + " " + list[6:12]) #Humpty Dumpty

#2.Given: Two positive integers a and b (a<b<10000).
#Return: The sum of all odd integers from a through b, inclusively.
num1 = 100
num2 = 200
sum = int()
for i in range(num1, num2):
    if i % 2 != 0:
        sum += i
#print(sum) 75000

#3. Reading and writing:
f = open('output.txt', 'w')
f.write('Bravely bold Sir Robin rode forth from Camelot\n' \
'Yes, brave Sir Robin turned about\n' \
'He was not afraid to die, O brave Sir Robin\n' \
'And gallantly he chickened out\n' \
'He was not at all afraid to be killed in nasty ways\n' \
'Bravely talking to his feet\n' \
'Brave, brave, brave, brave Sir Robin\n' \
'He beat a very brave retreat')

f.close()

with open("output.txt", "r") as f:
    for line_num, txt in enumerate(f):
        if line_num % 2 != 0:
            print(txt)


#4. working with dict():
s = "We tried list and we tried dicts also we tried Zen"
out = dict()
for words in s.split():
    if words not in out:
        out[words] = 1
    else:
        out[words] += 1

print(out)

#5. Counting DNA nucleotide: - count a, count t, count g, and count c:
dna_s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
count_a = int()
count_c = int()
count_g = int()
count_t = int()

for nu in dna_s:
    if nu == "C":
         count_c += 1
    else:
        if nu == "A":
           count_a += 1
        elif nu == "T":
           count_t += 1
        else: 
           count_g += 1

print(count_a)
print(count_c)
print(count_g)
print(count_t)

#6. Transcribe DNA to RNA:
dna_str = "GATGGAACTTGACTACGTAAATT"
rna_str = dna_str.replace("T", "U")
print(rna_str)

#7. Complementing a Strand of DNA
sense_dna = "AAAACCCGGT"
def complement(dna):
    dna_rev = dna[::-1]
    table = str.maketrans("ATGC", "TACG")
    return(dna_rev.translate(table))

print(complement(sense_dna))

  
#8. Wascally Wabbits
n =5 # 5th month
k = 3 #number of infant each time;

adult = int()
infant = 1
repro= int()

for i in range(1, n):
    repro = adult + repro
    adult = infant 
    infant = repro * k

#print(repro+adult+infant)

#9.C Computing GC Content:
#3. Reading and writing:
f = open('output.fasta', 'w')
f.write('>Rosalind_6404\n' \
'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG\n' \
'>Rosalind_5959\n' \
'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC\n' \
'>Rosalind_0808\n' \
'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT')

f.close()
with open("output.fasta", "r") as f:
    it = iter(f)
    max_GC_content = float()
    max_id = ""
    for line1, line2 in zip(it, it):
        tag = line1
        seq = line2
        GC_count = int()
        for i in seq:
            if i == "G" or i == "C":
                GC_count+=1
            GC_content = GC_count/len(seq)
            if GC_content > max_GC_content:
                max_GC_content = GC_content
                max_id = tag
    print(tag)
    print(max_GC_content)
   
#10. Hamming distance:
dna1 = "GAGCCTACTAACGGGAT"
dna2 = "CATCGTAATGACGGCCT" 

h_dist = int()
for s1, s2 in zip(dna1, dna2):
    if s1 != s2:
        h_dist += 1
    else:
        h_dist = h_dist
print(h_dist)

""" 
#11. Mendel's 1st Law:
n = 2 #aa
k = 2 #AA
m = 2 #Aa

#calculate for the selection probability:
#pair 1 prob:
popul = n + k + m
prob_m1 = m / popul #if pick 1 is m
prob_k1 = k / popul #if pick 1 is k
prob_n1 = n / popul #if pick 1 is n

prob_1_ls = {"m" : prob_m1, 
             "k" : prob_k1, 
             "n" : prob_n1}

prob_2_ls = {"m" : m, 
            "k" : k, 
            "n" : n}

double_prob = {}
single_prob = {}
for pick, prob in prob_1_ls.items():
    for pick2, num2 in prob_2_ls.items():
        #calculate for those with doubles: mm, kk, nn
        if pick2 == pick:
            p = (num2 - 1) / (popul - 1)
            double_prob[f"{pick}{pick2}"] = p
        #calculate for those with unique single : km, mn, etc.
        else:
            prob = prob = num2 / (popul - 1)
            single_prob[f"{pick}{pick2}"] = p
            #single_prob = num2 / (popul - 1)
            
print(double_prob)    
print(single_prob) 

#
               
   
    








    

                   
               
    
    


