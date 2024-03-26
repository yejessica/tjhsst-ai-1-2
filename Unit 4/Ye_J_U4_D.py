import sys; args = sys.argv[1:]
# print(args)
idx = int(args[0])-60

myRegexList = [
    r"/^((?!010)[01])*$/",
    r"/^((?!010|101)[01])*$/",
    r"/^([01])([01]*\1)?$/",
    r"/\b(?!(\w)+\w*\1\b)\w+\b/i",
    r"/\b(?:(?:\w*(\w)\w*(\w)\w*\1\w*\2\w*)|(?:\w*(\w)\w*\3\w*(\w)\4\w*)|(?:\w*(\w)\w*(\w)\w*\6\w*\5\w*))\b/i",
    r"/\b(?!(?!(?:\w*(\w)\w*\1\w*))\w*|Penn|del)(?=\w*(\w)\w*(\2\w*){2,})\w*\b/i",
    r"/\b(?!\b\w*([aeiou])\w*\1\w*\b)(?=\w*?a)(?=\w*?e)(?=\w*?i)(?=\w*?o)(?=\w*?u)\w+\b/i",
    r"/^(11|00|(10|01)(11|00)*(01|10))*(0|(10|01)(00|11)*1)$/",
    r"/^(0|(1(01*0)*10*)+)$/",
    r"/^(?!^(0|(1(01*0)*10*)+$))[01]+$/",
]


print(myRegexList[idx])

#Jessica Ye, 5, 2023