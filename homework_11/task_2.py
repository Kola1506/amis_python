def nino(list):
    if len(list) == 1:
        return str(list[0])
    else :
        return str(nino(list[1:]))+" "+str(list[0])



list  = []
bos = 0
while bos ==0 :
    x = input("Enter number :")
    if x.lower() == "":
        bos = 1
    else :
        list.append(x)

print(nino(list))
input()
