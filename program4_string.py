a=str(input("primul cuvant: "))
b=str(input("al doilea cuvant: "))
c=str(input("al treilea cuvant: "))
d=str(input("al patrulea cuvant: "))
m=str(a)
o=str(b)
l=str(c)
p=str(d)
n=0
if(((len(m))>=3)and((len(o))>=3)and((len(l))>=3)and((len(p))>=3)):
    n=(len(p))/2
    i=int(n)
    j=m[:2]
    k=o[0]
    h=l[:3]
    g=p[:i]
    print(a,b,c,d, sep="  ")
    print(str(j)+str(k)+str(h)+str(g))
else:
    print("nu corespunde conditiei")