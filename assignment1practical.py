import logging
logging.basicConfig(filename="assignment.log",level=logging.DEBUG)


#Write a program to print "Hello Python"?
print("Hello Python")

#Write a Python program to do arithmetical operations addition and division?
def addition():
    a = int(input("enter first digit"))
    b = int(input('enter second digit'))
    return a+b

def multiplication(a,b):
    a = int(input("enter first digit"))
    b = int(input('enter second digit'))
    return a/b

# Write a Python program to find the area of triangle?
def area_of_triangle(a, b, c):
    try:
        a = int(input("enter first side"))
        b = int(input("enter second side"))
        c = int(input("enter third side"))
        s = (a + b + c) / 2
        print(s * (s - a) * (s - b) * (s - c)) **1/2
    except exception as e :
        logging.exception(e)

#Write a python program to swap two variables?
def swap():
    try:
        a = int(input("enter first digit"))
        b = int(input('enter second digit'))
        temp=a
        a=b
        b=temp
        logging.info(a)
        logging.info(b)
    except exception as e:
        logging.exception(e)

#Write a Python program to generate a random number?
def random():
    try:
        a = int(input("enter first digit"))
        b = int(input('enter second digit'))
        return (random.randint(a,b))
    except exception as e:
        logging.exception(e)

