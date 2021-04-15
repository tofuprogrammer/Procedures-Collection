def count(num):
    start = 0
    if num > 100:
        print("Error, number must be equal to or less than 100")
    else:
        for i in range(1, num + 1):
            start += 1
            print(start)


count(int(input("Enter a number")))
