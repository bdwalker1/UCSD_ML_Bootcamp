from icecream import ic
import array


l: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l.pop()
l.sort(reverse=True)
l.pop()
ic(l)
l[0], l[1], l[2], l[3] = l[1], l[0], l[3], l[2]
ic(l)

a = array.array('i', [])
for i in range(100):
    a.append(i)
a.append('a')
ic(a)

