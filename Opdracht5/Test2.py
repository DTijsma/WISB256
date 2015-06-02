from Vector import *

u0=Vector(3)
#print(u0)

u1 = Vector(3,3.14)
#print(u1)

u2 = Vector(3,[2.0, 3.14, -5])
#print(u2)
u = Vector(3,[1,2,3])
v = Vector(3,3.5)
w = u.lincomb(v,10,1)
#print(w)
w = w.scalar(2)
#print(w)

#print(w.norm())
#print(w.inner(u))

v0 = Vector(2,[3,1])
v1 = Vector(2,[2,2])
W = GrammSchmidt([v0,v1])
print(W[0])
print(W[1])

print(W[0].inner(W[1]))
print(W[0].norm())


#v0 = Vector(4,[3,1,5,6])
#v1 = Vector(4,[3,1,5,7])
#v2 = Vector(4,[3,1,6,7])
#v3 = Vector(4,[3,2,5,7])
#W = GrammSchmidt([v0,v1,v2,v3])
#print(W[3])