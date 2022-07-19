import logging
logging.basicConfig(filename="practical.log",level=logging.DEBUG)


#Write a python program to convert kilometers to miles?
try:
    n=int(input("enter a number"))
    #conversion factor
    conv_fac=0.621371
    miles=n*conv_fac
    logging.info(miles)
except exception as e:
    logging.exception(e)

#Write a program to convert Celsius to fahrenheit?
try:
    celsius=int(input("enter temp. in degree celsius"))
    #formula to convert celsius to fahrenheit
    fahrenheit=(celsius*9/5)+32
    logging.info(fahrenheit)
except exception as e:
    logging.exception(e)

#write a python program to display calender?
try:
    import calendar
    yy=int(input("enter year"))
    mm=int(input("enter month"))
    #to display calender
    logging.info(calender.month(yy,mm))
except exception as e:
    logging.exception(e)

#Write a program to slove a quadratic equation?
try:
    a=int(input("enter value of a from your quadratic equation "))
    b= int(input("enter value of b from your quadratic equation "))
    c = int(input("enter value of c from your quadratic equation "))
    #to solve quadratic equation
    sum1=-b+(b**2-4*a*c)**0.5/2*a
    sum2=-b-(b**2-4*a*c)**0.5/2*a
    logging.info(sum1)
    logging.info(sum2)
except exception as e:
    logging.exception(e)

#Write a python program to swap two variables without temp variable?
try:
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    #to swap two numbers
    a,b=b,a
    logging.info(a)
    logging.info(b)
except exception as e:
    logging.exception(e)