numbers = list(range(1, 51))
for i in range(len(numbers)):
    if numbers[i] % 3 == 0 and numbers[i] % 5 == 0:
        numbers[i] = "FizzBuzz"
    elif numbers[i] % 3 == 0:
        numbers[i] = "fiz"
    elif numbers[i] % 5 == 0:
        numbers[i] = "buzz"
    else:
        print(numbers[i])

print(numbers)
