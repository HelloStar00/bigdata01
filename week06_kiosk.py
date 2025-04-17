# 1) 아아 : 2000원 2) 라떼 : 2500원
prise = [1500, 2500]
while True :
    menu = input(f"1) 아이스아메리카노 {prise[0]}원 2) 카페라떼 {prise[1]}원 3) 주문 종료 : ")
    if menu == "1" :
        print(f"아이스 아메리카노를 주문하셨습니다. 가격은 {prise[0]}원 입니다")
    elif menu == "2":
        print(f"카페 라떼를 주문하셨습니다. 가격은 {prise[1]}원 입니다")
    elif menu == "3":
        print("주문을 종료합니다")
        break