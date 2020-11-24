s=str(input("introduceti un cuvant: "))
vocale=0
silabe=0
#dacă în fiecare silabă este numai o vocală, atunci numărul vocalelor va fi egal cu numărul silabelor
for i in s:
    if ((i=='a') or (i=='ă') or (i=='Î') or (i=='â') or (i=='î') or (i=='Â') or (i=='Ă')or (i=='e') or (i=='i') or (i=='o') or (i=='u') or (i=='A') or (i=='E') or (i=='I') or (i=='O') or (i=='U')):
        vocale+=1
        silabe=vocale
print('numarul silabelor este egal cu: ',silabe,)