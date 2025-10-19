#program to check if int input of user between 0 and 100 is in the fibonacci sequence


def user_input():
    while(1):
        try:
            x = int(input("Enter a number: "))
            if x <= 100:
                return x
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a number.")


def fibonacci():
    fib = []
    for i in range(12):
        if i == 0:
            fib.append(0)
            continue
        elif i == 1:
            fib.append(1)
            continue
        else:
            fib.append(fib[-1] + fib[-2])
    return fib

def check_fib(x):
    if x in fibonacci():
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