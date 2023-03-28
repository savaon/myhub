"""import random
uppercaseLetter = chr(random.randint(65,90))
if uppercaseLetter == True:
    print=int("uppercaseLetter")"""

# dayx = ord("M")
# dayx1 = chr(int("75"))
# print(dayx)
# print(dayx1) cyfry albo literki z tablicy ACSC II

# comment block of the lines Cntrl + /

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
import random
uppercaseLetter1 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2 = chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercareLetter1 = chr(random.randint(65,90)) #Generate a radom chr from table but lower cases
lowercareLetter2 = chr(random.randint(65,90))
digit1 = chr(random.randint(0,9))
digit2 = chr(random.randint(0,9))
punctuationSign1 = chr(random.randint(128,191))
punctuationSign2 = chr(random.randint(128,191))
password = uppercaseLetter1 + uppercaseLetter2 + lowercareLetter1 + lowercareLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2
shuffle(password)
print(password)