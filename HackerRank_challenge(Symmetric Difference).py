a = raw_input()
b = raw_input()
c = raw_input()
d = raw_input()

e = list(map(int, a.split()))
f = list(map(int, b.split()))
g = list(map(int, c.split()))
h = list(map(int, d.split()))

i = [x for x in set(e).difference(set(g))] + [y for y in set(g).difference(set(e))]
j = [u for u in set(f).difference(set(h))] + [v for v in set(h).difference(set(f))]
w = [o for o in set(j).difference(set(i))]
for s in sorted(w):
    print s

