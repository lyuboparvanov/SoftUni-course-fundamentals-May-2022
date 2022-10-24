def isprime(number):
    if number > 1:
        for num in range(2, number):
            if number % num == 0:
                print(f"False")
                break
        else:
            print("True")

number = int(input())
isprime(number)