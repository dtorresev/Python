hrs = input("Enter Hours:")
h = float(hrs)
   
rate = input("Enter rate:")
r = float(rate)

if h > 40:
    extra_hours = h%40
    normal_hours = h-extra_hours
   # print(extra_hours)
    extra_pay = (r*1.5)*extra_hours
else :
    extra_pay = 0

#print(r)
#print(h)
pay = normal_hours*r + extra_pay
print(pay)