#program to check if int input of user between 0 and 100 is in the fibonacci sequence


def user_input():
    while(1):
        try:
            x = int(input("Enter a number: "))
            if 0<= x <= 100:
                return x
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def fibonacci(n):
    a, b = 0, 1
    while(a <= 100):
        if(a==n):
            return True
        a, b = b, a+b
    return False

def check_fib(x):
    if fibonacci(x):
        print("This is a fibonacci number")
    else:
        print("This number is not a fibonacci number.")

def retry():
    redo = input("Try again?(y/n):").lower()
    if redo == "y":
        return True
    else:
        return False

def main():
    while True:
        x = user_input()
        check_fib(x)
        if not(retry()):
            print("Goodbye!")
            break

main()