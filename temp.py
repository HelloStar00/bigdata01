try:
    a = int(input())
    b = int(input())

    print(a / b)
except ValueError as err :
    print(f"{err} : int인데 다른 값이 들어갔을 때")
except ZeroDivisionError as err:
    print(f"{err} : 나누는 값이 0을 넣었을 때")
except Exception as err :
    print(f"{err} : 모든 오류 구문을 잡음")
