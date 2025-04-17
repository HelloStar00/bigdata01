# 1) 아아 : 2000원 2) 라떼 : 2500원
drink = ["아이스 아메리카노", "카페 라떼"]
prise = [1500, 2500]
while True :
    menu = input(f"1) {drink[0]} {prise[0]}원 2) {drink[1]} {prise[1]}원 3) 주문 종료 : ")
    if menu == "1" :
        print(f"{drink[0]}를 주문하셨습니다. 가격은 {prise[0]}원입니다.")
    elif menu == "2":
        print(f"{drink[1]}를 주문하셨습니다. 가격은 {prise[1]}원입니다")
    elif menu == "3":
        print("주문을 종료합니다")
        break