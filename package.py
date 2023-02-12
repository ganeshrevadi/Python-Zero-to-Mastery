from collections import Counter,defaultdict,OrderedDict

li = [1,2,3,4,5,6]
sentence = 'blah blanb akjhkldjf hkjk adkf '

print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda:5,{'a':1,'b':2})
print(dictionary['c'])
print(dictionary['a'])


#Dict are ordered by default

d1 = {'c' :100}
d1['a'] = 1
d1['b'] = 1

d2 = {'c':100}
d2['b'] = 2
d2 ['a'] = 1

print(d1 == d2)

