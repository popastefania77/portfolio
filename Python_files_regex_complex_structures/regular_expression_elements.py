import re


"""
string = 'Python is a scripting language'


# ^ -> matches beginning of line
print(re.search('^Python', string))
# <re.Match object; span=(0, 6), match='Python'>
print(re.search('^is', string))
# None

# $ -> matches end of line
print(re.search('language$', string))
# <re.Match object; span=(22, 30), match='language'>
print(re.search('is$', string))
# None


# \A -> matches beginning of string
m = re.search('\APython', string)
print(m)
# <re.Match object; span=(0, 6), match='Python'>
print(m.group())
# Python
m = re.search('\Ascripting', string)
print(m)
# None


# \Z -> matches the end of string (if a newline exists, it matches just before newline)
m = re.search('language\Z', string)
print(m.group())
# language
m = re.search('Python\Z', string)
print(m)
# None


# \b -> matches word boudaries when outside brackets (matches backspace - 0x08 - when iside brackets)
m = re.search(r'\bPython\b', string)
print(m.group())
# Python
string2 = 'Python2 is a scripting language'
print(re.search(r'\bPython\b', string2))
# None


# \B -> matches nonword boundaries
string2 = 'Python2 is a scripting language'
m = re.search(r'Python\B', string2)
print(m.group())
# Python
"""


"""
string = 'Python is a scripting language?'

# (?:re) -> groups regular expressions without remembering matched text
mm = re.search(r'(Python) (?:.+)', string)
print(mm)
# <re.Match object; span=(0, 31), match='Python is a scripting language?'>
print(mm.group())
# Python is a scripting language?
print(mm.group(0))
# Python is a scripting language?
print(mm.group(1))
# Python
print(mm.group(2))
# IndexError: no such group


# (?#...) -> comment
m = re.search('Python(?#comment)', string)
print(m.group())
# Python


# (?=re) -> specifies position using a pattern (doesn't heve a range)
mm = re.search(r'language(?=\?)', string)
print(mm.group())
# language
print(mm.group(0))
# language
mm = re.search(r'language(?=!)', string)
print(mm)
# None


# (?!re) -> specifies position using pattern negation (doesn't heve a range)
mm = re.search(r'language(?!!)', string)
print(mm.group())
# language
print(mm.group(0))
# language
mm = re.search(r'language(?!\?)', string)
print(mm)
# None


# (?>re) -> matches independent pattern without backtarcking
m = re.search('(?<=abc)def', 'abcdef')
print(m.group())
# def
print(m.group(0))
# def
"""

