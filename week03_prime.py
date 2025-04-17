number = int(input())
isPrime = True

if number >= 2 :
    for i in range(1, number + 1) :
        if number % i == 0 :
            isPrime = True
        print(i, end=" ")
else :
    isPrime = False

if isPrime :
    print(f"\n{number}는(은) 소수입니다.")
else :
    print(f"\n{number}는(은) 소수가 아닙니다.")