# Anagrams

# Write a function, anagrams, that takes in two strings as arguments. 
# The function should return a boolean indicating whether or not the strings are anagrams. 
# Anagrams are strings that contain the same characters, but in any order.

def anagrams(s1, s2):
  if sorted(s1) == sorted(s2):
    print(True)
  else:
    print(False)

# def anagrams(s1, s2):
#     s1_letters = {}
#     s2_letters = {}
#
#     for letter in s1:
#         if letter in s1:
#             s1_letters[letter] += 1
#         else:
#             s1_letters[letter] = 1
#
#     for letter in s2:
#         if letter in s2:
#             s2_letters[letter] += 1
#         else:
#             s2_letters[letter] = 1





# TEST CASES
# anagrams('restful', 'fluster') # -> True
# anagrams('cats', 'tocs') # -> False
# anagrams('monkeyswrite', 'newyorktimes') # -> True
# anagrams('paper', 'reapa') # -> False
# anagrams('elbow', 'below') # -> True
# anagrams('tax', 'taxi') # -> False
# anagrams('taxi', 'tax') # -> False
# anagrams('night', 'thing') # -> True
# anagrams('po', 'popp') # -> False
# anagrams('pp', 'oo') # -> False
