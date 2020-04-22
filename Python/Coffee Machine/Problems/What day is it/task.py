zone = int(input())
day = 10.30 + zone

if day <= 0:
    print("Monday")
elif 0 < day <= 24:
    print("Tuesday")
else:
    print("Wednesday")
