b = [ "apple","man","kam","apple"]#set ma indexibfg layera nikalnu mildaina

set1 = set(b)
print(set1)

c = set()
print(c)

d = {1,0,True,False,"a","b"}
print(d)
d.add(4)
print(d)
d.remove("a")
print(d)
d.discard(1)
print(d)
#del d
print(d)
d.pop()
print(d)
x = d.pop()
print(x)
set1 = {1,2,3,4}
set2 = {1,2,5,7,8}
#set5=set1.union(set2)#total dinxa plus garera
#print(set5)
#set4 = set1|set2#union ho hai
#print(set4)
set0=set1.intersection(set2)
print(set0)#yesley chai duita ko same matra COMMON NIKALXA ra update vnda farak xa naya variable chainxa

#set1.update(set2)
#print(set1)#yesley chai add garxa update ley naya variable pardina

#set1.intersection_update(set2)#UPDATE GARYO VANEY SAME vako gayera set1 ma basxa aru falxa
#print(set1)
set6= set1&set2
print(set6)#
set3=set2.difference(set1)#jun agadi aayo tesko value ko baki vako rakhxa
#set3 = set2 - set1#same hio
print(set3)
set1.difference_update(set2)
print(set1)
set7=set1.symmetric_difference(set2)#yo vaneko common bahek sabai dey
#set7 = set1^set2#same ho
print(set7)
set1.symmetric_difference_update(set2)
print(set1)
b = set1.isdisjoint(set2)
print(b)
c = set1.issuperset(set2)
#d = frozenset(set1)#yesley chai froze garxa
print(c)



