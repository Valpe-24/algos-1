# Decompress

# Write a function, decompress, that takes in a string as an argument. 
# The input string will be formatted into multiple groups according to the following pattern:

# <number><char>
# for example, '2c' or '3a'.

# The function should return an decompressed version of the string where each 'char' of a group 
# is repeated 'number' times consecutively. 
# You may assume that the input string is well-formed according to the previously mentioned pattern.

def decompress(s):
    result = []
    i = 0; j = 0
    numbers = '0123456789'

    while j < len(s): 
        if s[j] in numbers: 
            j += 1
        else: 
            num = int(s[i:j])
            result.append(num * s[j])
            j += 1
            i = j

    return ''.join(result)
    




# TEST CASES
print(decompress("2c3a1t")) # -> 'ccaaat'
print(decompress("4s2b")) # -> 'ssssbb'
print(decompress("2p1o5p")) # -> 'ppoppppp'
print(decompress("3n12e2z")) # -> 'nnneeeeeeeeeeeezz'
print(decompress("127y")) # -> 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'


# def decompress(s):
#     letters = []
#     nums = []
#     just_letters = []

#     for char in s: 
#         if char.isalpha():
#             letters.append(char)
#         elif s[s.index(char) - 1].isdecimal(): 
#             int(char).join(s[s.index(char) - 1])
#         else: 
#             nums.append(char)

#     print(letters)
#     print(nums)

#     for letter in letters: 
#         for _ in range(nums[letters.index(letter)]):
#             just_letters.append(letter)
            

#     print(''.join(just_letters))


# def decompress(s):
#     letters = []
#     nums = []
#     just_letters = []

#     for char in s: 
#         if char.isalpha():
#             letters.append(char)

#         else: 
#             nums.append(int(char))

#     print(letters)
#     print(nums)

#     for letter in letters: 
#         for _ in range(nums[letters.index(letter)]):
#             just_letters.append(letter)
            

#     print(''.join(just_letters))