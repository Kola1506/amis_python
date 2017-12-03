def bbc(list):
    if len(list) == 1 :
        return list[0]
    if list[0] < bbc(list[1:]):
        return list[0]
    else :
        return bbc(list[1:])


list  = []
bos = 0
while bos ==0 :
    x = input("Enter number :")
    if x.lower() == "":
        bos = 1
    else :
        list.append(x)



print(bbc(list))
input()
