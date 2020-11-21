str=input("introduceti un sir de caractere: ")
majuscule=0
cifre=0
for i in str:
    majuscule+=i.isupper()
print('in sir sunt: ',majuscule, 'majuscule')
for i in str:
    cifre+=i.isdecimal()
print('in sir sunt: ',cifre, 'cifre')
