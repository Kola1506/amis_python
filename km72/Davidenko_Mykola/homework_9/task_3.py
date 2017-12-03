print("---Hello---")
def power(a,n):
    if n == 1 :
        return a
    else :
        return a * power(a, n-1)
x = float(input("Enter x : "))
y = int(input("Enter y : "))
print(power(x,y))
print("---end---")
input()
