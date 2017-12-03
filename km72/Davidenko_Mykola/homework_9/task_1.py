print("---Hello---")
def distance(q1, w1, q2,w2):
    d = ((q2-q1)**2+(w2-w1)**2)**0.5
    print(d)
x1 = float(input("Enter x1 :"))
y1 = float(input("Enter y1 :"))
x2 = float(input("Enter x2 :"))
y2 = float(input("Enter y2 :"))
distance(x1,y1,x2,y2)
input()
