#Circle project:My first project with the help of the Internet
#پروژه دایره:اولین پروژه من با کمک اینترنت
#
#Import pi from the Python math library
#وارد کردن عدد پی از کتابخانه ریاضی پایتون
from math import pi

print("Enter the size of the radius:")

#Radius=r
#شعاع=r
#
#We request the size of the radius with the input command
#اندازه شعاع را با دستور اینپوت درخواست می کنیم
r = float(input("Radius:")) 

#Area of ​​circle:
#مساحت دایره:
S = pi * (pow(r,2)) 
#You can also find the area with the commented command below
#می توان با دستور کامنت شده زیر نیز مساحت را پیدا کرد
#
# S = pi * (r**2)

#perimeter of the circle: 
#محیط دایره:
P = 2*pi*r

print("Area of ​​circle:")
print(S)
print("perimeter of the circle:")
print(P)
