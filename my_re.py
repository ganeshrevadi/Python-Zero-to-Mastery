import re

pattern = re.compile('this')
pattern2 = re.compile('search it inside of this string please')
string = 'search it inside of this string please'

a = pattern.search(string)
b= pattern.findall(string)
c = pattern2.fullmatch(string)
d = pattern.match(string)


print(a)
print(b)
print(c)
print(d)