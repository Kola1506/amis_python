X = int(input("Enter minutes : "))
minutes = X % 60
day = X % 1440
hour = day // 60
print('Time: {0:02d}:{1:02d}'.format(hour, minutes))
input()
