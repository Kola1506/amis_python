print("---Hello---")
def power(a,n):
    if n > 0:  
        r = 1
        a1 = a
        while r < n:
            a = a*a1
            r = r+1
        print(a)
    elif n < 0:
        r = 0
        a1 = a
        while r > n:
            a = a/a1
            r = r-1
        print(a)
    elif n == 0:
        print(1)
    elif a == 0:
        print(0)
x = float(input("Enter x :"))
y = float(input("Enter y :"))
power(x ,y)
print("---End---")
input()
