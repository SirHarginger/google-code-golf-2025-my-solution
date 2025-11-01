def p(a):
 b=sum(a,[])
 if min(b)==max(b):return[[5]*3,[0]*3,[0]*3]
 l,m,r=zip(*a)
 f=lambda c:(c[0],.5)if c[0]==c[1]else((c[1],1.5)if c[1]==c[2]else((c[0],1)if c[0]==c[2]else(0,0)))
 L,la=f(l);M,_=f(m);R,ra=f(r)
 d=[[5,0,0],[0,5,0],[0,0,5]]
 return d if L and R and((L==R and la>=ra)or(L!=R and M in(L,R)))else[x[::-1]for x in d]
