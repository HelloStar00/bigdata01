number = int(input())
isPrime = True

if number >= 2 :
    i = 2
    while i * i <= number :
        if number % i == 0 :
            isPrime = True
        print(i, end=" ")
        i = i + 1
else :
    isPrime = False

if isPrime :
    print(f"\n{number}는(은) 소수입니다.")
else :
    print(f"\n{number}는(은) 소수가 아닙니다.")