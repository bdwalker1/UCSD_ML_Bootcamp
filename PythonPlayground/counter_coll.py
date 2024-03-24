import collections
from collections import Counter

c = Counter('This is a sentence that I am passing into a counter.'.lower())
print(c.most_common(2))
c = Counter(['a', 'b', 'b', 'b', 'c', 'c'])
print(c)
c = Counter(a=30, b=50, c=75)
print(c)
