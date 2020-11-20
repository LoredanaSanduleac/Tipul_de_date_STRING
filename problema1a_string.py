str=input("introduceti un sir de caractere: ")
majuscule=0
for i in range(len(str)):
    if(str[i]>='A' and str[i]<='Z'):
        majuscule+=1
print('in sir sunt: ',majuscule, "majuscule")