#Exercise 1 - verify if a number is a prime number

num = int(input("please enter a number: "))  #1047


if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num//i, "is", num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num, "is not a prime number")