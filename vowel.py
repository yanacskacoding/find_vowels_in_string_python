
'''Define a function isVowel(char) that returns True if char is a vowel ('a', 'e', 'i', 'o', or 'u'), and False otherwise. You can assume that char is a single letter of any case (ie, 'A' and 'a' are both valid).

Do not use the keyword in. Your function should take in a single string and return a boolean.

def isVowel(char):

 

    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.



    # Your code here


char = input()

**Include input at the end of the program like shown above.

Example:
 isVowel('a')
    True
 isVowel('b')
    False
 isVowel('A')
    True
 isVowel('Z')
    False
    
    '''

#Code:

def remove_special_chars(thisString):
    return(''.join(e for e in thisString if e.isalnum()))

def isVowel(char):
    if char.isalpha():
        char = char.lower()
        if char == 'a' or char == 'e' or char =='i' or char == 'o' or char == 'u':
            return True
    return False

char = input()
char = remove_special_chars(char)

print(isVowel(char))