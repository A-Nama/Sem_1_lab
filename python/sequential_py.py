# -*- coding: utf-8 -*-
"""sequential.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AVWRgX2TAxNatvHdH0bdcinbeBxl5RN_
"""

print("PROGRAM 1")
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
sum=a+b
print("The sum of two numbers is ", sum)

print("PROGRAM 2")
b=int(input("Enter base of triangle: "))
h=int(input("Enter height of triangle: "))
area=0.5*b*h
s1=int(input("Enter length of 1st side: "))
s2=int(input("Enter length of 2nd side: "))
s3=int(input("Enter length of 3rd side: "))
perimeter=s1+s2+s3
print("The area of the triangle is ", area)
print("The perimeter of the triangle is ", perimeter)

print("PROGRAM 3")
r=int(input("Enter radius of triangle: "))
area=3.14*r*r
print("The area of the circle is ",area)

print("PROGRAM 4")
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter another number: "))
sum=a+b+c
avg=sum/3
print("The sum of the numbers is ",sum , "and their average is ", avg)

print("PROGRAM 5")
td=int(input("Enter number of days: "))
y=td//365
m=(td%365)//30
d=td-((y*365)+(m*30))
print(y," years, ", m," months and ", d, " days.")

print("PROGRAM 6")
s=int(input("Enter seconds: "))
h=s//3600
s-=h*3600
m=s//60
s-=m*60
print(h, " hours, ", m, " minutes and ", s, " seconds.")

print("PROGRAM 7")
a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
sum=a+b
diff=a-b
prod=a*b
quo=a/b
print("The two numbers sum is ", sum, " product is ", prod, " difference is ", diff, " and quotient is ", quo)

print("PROGRAM 8")
b=int(input("Enter b coefficient: "))
a=int(input("Enter a coefficient: "))
c=int(input("Enter constant c: "))
d=b**2-4*a*c
r1=((-b)+(d**0.5))/2*a
r2=((-b)-(d**0.5))/2*a
print("The roots are ", r1, " and ", r2)

print("PROGRAM 9")
s1=int(input("Enter marks of first subject: "))
s2=int(input("Enter marks of second subject: "))
s3=int(input("Enter marks of third subject: "))
s4=int(input("Enter marks of fourth subject: "))
s5=int(input("Enter marks of fifth subject: "))
sum=s1+s2+s3+s4+s5
perc=(sum/500)*100
print("The overall percent scored is ", perc)

print("PROGRAM 10")
c=int(input("Enter temperature in celsius: "))
temp=c*(9/5)+32
print("The temperature is ", temp, "C")