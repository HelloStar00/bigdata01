number = int(input())
count = 0

if number >= 2 :
    for i in range(1, number + 1) :
        if number % i == 0 :
            count = count + 1
        print(i, end=" ")
else :
    count = 1

if count == 0 :
    print(f"\n{number}는(은) 소수입니다.")
else :
    print(f"\n{number}는(은) 소수가 아닙니다.")