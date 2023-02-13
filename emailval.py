import re 

pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b")

string = "ganesh@gamil.com"

string2 = "ganesh"

a = pattern.search(string)
print(a)
 
b = pattern.search(string2)
print(b)