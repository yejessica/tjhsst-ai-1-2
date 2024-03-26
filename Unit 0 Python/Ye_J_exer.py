# Name: Jessica Ye
# Date: 9/8/21
# Do not forget to change the file name -> Save as

''' Tasks '''

from PIL import Image
# msg = input("nums: ")
# print (msg)
# print (msg.split())
# print ([int(x) for x in msg.split()]) #list comprehension

# 1. Given an input of a space-separated list of any length of integers, output the sum of them.
number12 = input("list of numbers: ")
print ("1. sum =", sum([int(x) for x in number12.strip().split()])) # #1

# print (sum([int(x) for x in input("list of numbers: ").strip().split()])) # #1

# 2. Output the list of those integers (from #1) that are divisible by three.
print ("2. list of multiples of 3:" , [int(x) for x in number12.strip().split() if int(x) % 3 == 0]) # #2

# 3. Given an integer input, print the first n Fibonacci numbers. eg. n=6: 1, 1, 2, 3, 5, 8
def fibonacciSeq(n):
    seq = [0,1]

    for i in range (2, n+1):
        seq.append(seq[-1] + seq[-2])

    return seq[1:]

print ("3. fibonacci:", " ".join(map(str, fibonacciSeq(int(input("Type n for Fibonacci sequence: ").strip())))))

# 4. Given an input, output a string composed of every other character. eg. Aardvark -> Arvr
print("4. every other str:", input("Type a string: ").strip()[::2])


# 5. Given a positive integer input, check whether the number is prime or not.
def primeCheck(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n%i)==0: return False
        return True
    else: return True

print("5. Is Prime?", primeCheck(int(input("Type a number to check prime: ").strip())))

# 6. Calculate the area of a triangle given three side lengths.  eg. 13 14 15 -> 84
triangleSides = [int(x) for x in input("Type three sides of a triangle: ").strip().split()]

def triArea(ar):
    s = int(sum(ar)/2)
    a = (s*(s-ar[1])*(s-ar[2])*(s-ar[0]))**(1/2)
    return a

print("6. The area of", " ".join(map(str,triangleSides)), "is", triArea(triangleSides))

# 7. Given a input of a string, remove all punctuation from the string. 
# eg. "Don't quote me," she said. -> Dontquotemeshesaid
# stringTranslated = input("Type a sentence: ").translate(str.maketrans('','', string.punctuation)).translate({ord(c): None for c in string.whitespace})
stringTranslated = input("Type a sentence: ").strip()

punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for c in punct:
    if c in punct:
        stringTranslated = stringTranslated.replace(c, "")

stringTranslated = stringTranslated.replace(" ", "")

print("7. Punct removed:", stringTranslated)

# 8. Check whether the input string (from #7, lower cased, with punctuation removed) is a palindrome.
print("8. Is palindrome?", stringTranslated.lower()[::-1] == stringTranslated.lower())

# 9. Count the number of each vowel in the input string (from #7).
def countVowel(s):
    vowelCounts = {}
    for v in "aeiou": vowelCounts[v] = s.count(v)
    return vowelCounts
print("9. Count each vowel:", countVowel(stringTranslated))

# 10. Given two integers as input, print the value of f\left(k\right)=k^2-3k+2 for each integer between the two inputs.  
# eg. 2 5 -> 0, 2, 6, 12
ranges = [int(i) for i in input("Type two integers (lower bound and upper bound): ").strip().split()]
print("10. Evaluate f(k)=k^2 - 3k + 2 from", ranges[0], "to", ranges[1], ":", " ".join(map(str, [(i**2-3*i+2) for i in range(ranges[0],ranges[1]+1)])))

# 11. Given an input of a string, determines a character with the most number of occurrences.
str11 = input("Type a string: ").strip()

# def mostChar(s):
#     charCounts = {}
#     for c in "abcdefghijklmnopqrstuvwxyz": charCounts[c]=s.count(c)
#     mostOccur = max(charCounts.values())
#     returnArr = []

#     for key, value in charCounts.items():
#         if value == mostOccur:
#             returnArr.append(key)
#     return " ".join(returnArr)
def mostChar(s):
    charCounts = {}
    for c in "abcdefghijklmnopqrstuvwxyz": charCounts[c]=s.count(c)
    mostOccur = max(charCounts.values())
    returnArr = []

    for key, value in charCounts.items():
        if value == mostOccur:
            returnArr.append(key)
    
    for i in range(len(returnArr)-1):
        if s.index(returnArr[i])>s.index(returnArr[i+1]):
            # temp = returnArr[i+1]
            returnArr[i], returnArr[i+1] = returnArr[i+1], returnArr[i]
    return " ".join(returnArr)

print("11. Most occurred char: ", mostChar(str11))

# 12. With the input string from #11, output a list of all the words that start and end in a vowel.
str11Arr = str11.split()
print("12. List of words starting and ending with vowels:", [s for s in str11Arr if (s[-1].lower() in "aeiou" and  s[0].lower() in "aeiou")])

# 13. With the input string from #11, capitalizes the starting letter of every word of the string and print it.
print("13. Capitalize starting letter of every word:", " ".join([s.title() for s in str11Arr]))

# 14. With the input string from #11, prints out the string with each word in the string reversed.
print("14. Reverse every word:", " ".join([s[::-1] for s in str11Arr]))

# 15. With the input string from #11, treats the first word of the input as a search string to be found in the rest 
# of the string, treats the second word as a replacement for the first, and treats the rest of the input as the string to be searched.
# 	eg.    b Ba baby boy ->  BaaBay Baoy

def changeFirst(arr):
    find = arr[0]
    replace = arr[1]
    for i in range(2, len(arr)):
        if find in arr[i]:
            arr[i] = arr[i].replace(find, replace)

    return arr

print("15. Find the first and replace with the second:", " ".join(changeFirst(str11Arr)[2:]))
 
# 16. With an input of a string, removes all duplicate characters from a string.  Eg. detection -> detcion
# print("Remove all duplicate chars:", " ".join(map(str, set(input("Type a string to remove all duplicate chars: ").strip().replace(" ","")))))
removingDuplicates=input("Type a string to remove all duplicate chars: ").strip()
def removeDuplicate(str):
    s=set(str)
    s="".join(s)
    t=""
    for i in str:
        if (i in t):
            pass
        else:
            t=t+i
    return t
print("16. Remove all duplicate chars:", removeDuplicate(removingDuplicates))

# 17. Given an input of a string, determines whether the string contains only digits
checkNumString = input("Type a string to check if it has only digits or not: ").strip()
print("17. Is a number?:", checkNumString.isdecimal())

# 18. If #17 prints True, determines whether the string contains only 0 and 1 characters, and if so assumes it is a binary string, 
# converts it to a number, and prints out the decimal value.

def checkBinary(stringg):
    if  stringg.isdecimal():
        sett = set(stringg)
        s = {'0', '1'}
        return (s == sett or sett == {'0'} or sett == {'1'})

if checkBinary(checkNumString):
    print("18. It is a binary number:", int(checkNumString,2))
 
# 19. Write a script that accepts two strings as input and determines whether the two strings are anagrams of each other.

anagram1 = input("Type the first string to check anagram: ").strip().replace(" ","")
anagram2 = input("Type the second string to check anagram: ").strip().replace(" ","")

print("19. Are",anagram1 ,"and", anagram2, "anagram?:", sorted(anagram1) == sorted(anagram2))

# 20. Given an input filename, if the file exists and is an image, find the dimensions of the image.

f = input("Type the image file name: ")
img = Image.open(f)
width, height = img.size
print("20. Image dimnesion:",width, "by", height)
# print ("Image dimension:", img.size)

# 21. Given an input of a string, find the longest palindrome within the string.

def longestPaliStr(str):
    n = len(str)

    maximum = 1
    start = 0

    for i in range(n):
        for j in range(i, n):
            palindromeCheck = 1
            for k in range(0, ((j-i)//2)+1):
                if (str[i+k]!=str[j-k]):
                    palindromeCheck=0
            if (palindromeCheck!=0 and (j-i+1) > maximum):
                start = i
                maximum = j-i+1
    print("Longest palindrome within the string:", end=" ")
    for i in range(start, start+maximum):
        print(str[i], end="")

longestPaliString = input("Type a string to find the longest palindrome: ").strip().lower()
longestPaliString = longestPaliString.replace(" ", "")
longestPaliStr(longestPaliString)
print("")

# 22. Given an input of a string, find all the permutations of a string.
perms = []
def permute(arr, l, r):
    if l == r:
        # print ("".join(map(str, arr)))
        perms.append("".join(arr))
    else:
        for i in range(l, r):
            arr[l], arr[i] = arr[i], arr[l]
            permute(arr, l + 1, r)
            arr[l], arr[i] = arr[i], arr[l] 

permutationString = input("Type a string to do permutation: ").strip()

permute(list(permutationString), 0, len(permutationString))

print("22. All permutations:", perms)

# perms = [''.join(p) for p in permutations(input("Type a string to do permutation: ").strip())]
# print("All permutations:", perms)

# 23. Given the input string from #22, find all the unique permutations of a string.

print("23. All unique permutations:", set(perms))
 
# 24. Given an input of a string, find a longest non-decreasing subsequence within the string (according to ascii value).

def findIncSub(arr):
    increasingStrings = []
    increasingCheck = 1
    for i in range(1,len(arr)):
        if (ord(arr[i])<ord(arr[i-1])):
            increasingCheck = 0
        if (ord(arr[i])>ord(arr[i-1])):
            increasingCheck = 1
        if increasingCheck==1:
            increasingStrings.append(arr[i])
        else:
            increasingStrings.append(" ")
    # print(increasingStrings)
    allStrings = "".join(increasingStrings).split()
    # print(allStrings)
    return max(allStrings,key=len)

longestIncreasingStr = input("Type a string to find the longest non-decreasing sub: ").strip()
print("24. Longest non-decreasing sub:" , findIncSub(longestIncreasingStr))
