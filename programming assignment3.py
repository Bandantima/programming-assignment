import logging
logging.basicConfig(filename="programming.py",level=logging.DEBUG)


#Write a program to check if a Number is positive ,Negative or Zero?
try:
    num=int(input("enter a number"))
    if num==0:
        logging.info("it is a positive number")
    elif num<0:
        logging.info("it is a negative number")
    else:
        logging.info("it is a positive number")
except exception as e:
    logging.exception(e)

#Write a program to check if a number is odd or even?
try:
    num = int(input("enter a number"))
    if num%2==0:
        logging.info("it is a even number")
    else:
        logging.info("it is a odd number")
except exception as e:
    logging.exception(e)

#Write a python program to check Leap year?
try:
    year=int(input("enter a year"))
    #leap year comes once in 4 years
    if year%4==0:
        logging.info("it is a leap year")
    else:
        logging.info("it is not a leap year")
except exception as e:
    logging.exception(e)

#Write a python program to check prime number?
try:
    num=int(input("enter a number"))
    for i in range(2,10):
        if num%i==0:
            logging.info("it is not a prime no ")
        else:
            logging.info("it is a prime no ")
except exception as e:
    logging.exception(e)

#write a python program to print numbers in an interval of 1-10000?
try:
    for number in range(1, 10001):
        if number > 1:
            for i in range(2, 10000):
                if (number % i) == 0:
                    break
                else:
                    print(number)
except exception as e:
    logging.exception(e)
