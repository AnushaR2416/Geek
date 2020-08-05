#
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

      asks the user for two separate texts;
      checks whether, the entered texts are anagrams and prints the result.
      
#



s1=input()
s2=input()

s1.lower()
s2.lower()
s1.strip()
s2.strip()

NA=0
for s in s1:
    if s in s2:
        s2.replace(s,"",1)
    else:
        NA=1
        print("Not anagrams")
        break
if(NA==0):
    print("Anagrams")
