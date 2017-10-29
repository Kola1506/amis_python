print("---Hello---")
count = 1
a = input("Ведите рост учеников подряд через пробел : ").split()
for i in range(len(a)):
    a[i] = int(a[i])
print(a)
Peta = int(input("Ведите рост Пети : "))
for rost in a:
    if rost >= Peta:
        count += 1
print("Номер пети в сторою : ",count)
print("---End---")
