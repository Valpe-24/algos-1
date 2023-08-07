# Paired Parentheses

# Write a function, paired_parens, that takes in a string as an argument. 
# The function should return a boolean indicating whether or not the string has well-formed parentheses.
# You may assume the string contains only alphabetic characters, '(', or ')'.


def paired_parens(string):

  array = []

  for char in string: 

    if char == '(':
      array.append(char)

    elif char ==')' and array[-1]=='(':
      array.pop()
    
    
  if len(array) == 0: 
    return True
  else: 
    return False






# TEST CASES
print(paired_parens("(david)((abby))"))# -> True
print(paired_parens("()rose(jeff"))# -> False
# print(paired_parens(")(")) # -> False
print(paired_parens("()")) # -> True
print(paired_parens("(((potato())))")) # -> True
print(paired_parens("(())(water)()"))# -> True
