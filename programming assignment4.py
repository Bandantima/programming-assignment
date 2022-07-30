import logging
logging.basicConfig(filename="programming.log",level=logging.DEBUG)

#write a python program to find LCM?
def lcm():
    try:
        x=int(input("enter first num"))
        y=int(input("enter second num"))
        if x>y:
            x1=x-y
            lcm=x*y/x1
            logging.info(lcm)
        else:
            y1=y-x
            lcm=x*y/y1
            logging.info(lcm)
    except Exception as e:
        logging.exception(e)

#write a python program to find HCF?
def HCF():
    try:
        x = int(input("enter first num"))
        y = int(input("enter second num"))
        if x>y:
            x1=y
        else:
            x1=x
            for i in range(1,x1+1):
                if (x%i==0) and (y%i==0):
                    print(i)
    except Exception as e:
        logging.exception(e)

#Write a python program to convert decimal into binary,octal and hexadecimal?
def binary():
    try:
        x = int(input("enter your num"))
        if x>1:
            logging.info(bin(x))
    except Exception as e:
        logging.exception(e)

def octal():
    try:
        x = int(input("enter your num"))
        if x > 1:
            logging.info(oct(x))
    except Exception as e:
        logging.exception(e)

def hexadecimal():
    try:
        x = int(input("enter your  num"))
        if x > 1:
            y = hex(x)
            logging.info(y)
    except Exception as e:
        logging.exception(e)

#write a python program to find ASCII value of a character?
def ASCII():
    try:
        c=int(input('enter a character'))
        logging.info(ord(c))
    except Exception as e:
        logging.exception(e)

#Write a python program to make a simple calculator with 4 basic mathematical operations?
def calculator():
    try:
        # This function adds two numbers
        def add(x, y):
            logging.info(x+y)

        # This function subtracts two numbers
        def subtract(x, y):
            logging.info(x-y)

        # This function multiplies two numbers
        def multiply(x, y):
            logging.info(x*y)

        # This function divides two numbers
        def divide(x, y):
            logging.info(x/y)

        logging.info("Select operation.")
        logging.info("1.Add")
        logging.info("2.Subtract")
        logging.info("3.Multiply")
        logging.info("4.Divide")

        while(True):
            choice=int(input("enter your choice 1,2,3,4"))
            x = int(input("enter first number"))
            y = int(input("enter second number"))
            if choice == 1:
                logging.info(add(x,y))

            elif choice == 2:
                loging.info(subtract(x,y))

            elif choice == 3:
                logging.info(multiply(x,y))

            elif choice == 4:
                logging.info(divide(x,y))

            else:
                logging.info("Invalid Input")
    except Exception as e:
        logging.exception(e)

