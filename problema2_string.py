str=input("introduceti un sir de caractere: ")
majuscule=0
cifre=0
carspeciale=0
for i in range(len(str)):
    if(str[i]>='A' and str[i]<='Z'):
        majuscule+=1
print('in sir sunt: ',majuscule, 'majuscule')
for i in range(len(str)):
    if (str[i]>='0' and str[i]<='9'):
        cifre+=1
print('in sir sunt: ',cifre, 'cifre')


