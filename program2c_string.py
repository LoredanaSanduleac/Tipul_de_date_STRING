str=input("introduceti un sir de caractere: ")
cs=0
for i in str:
    if i.isalnum():
        continue
    if i.isspace():
        continue
    else:
        cs+=1     
print("in sir sunt: ",cs, "caractere speciale")