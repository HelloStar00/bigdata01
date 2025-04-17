# 1) 아아 : 2000원 2) 라떼 : 2500원
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스"]
price = [1500, 2500, 4000]
amounts = [0, 0, 0]
total_price = 0

while True :
    menu = input(f"1) {drinks[0]} {price[0]}원 2) {drinks[1]} {price[1]}원 3) {drinks[2]} {price[2]}원 4) 주문 종료 : ")
    if menu == "1" :
        print(f"{drinks[0]}를 주문하셨습니다. 가격은 {price[0]}원입니다.")
        total_price = total_price + price[0]
        amounts[0] = amounts[0] + 1
    elif menu == "2":
        print(f"{drinks[1]}를 주문하셨습니다. 가격은 {price[1]}원입니다")
        total_price = total_price + price[1]
        amounts[1] = amounts[1] + 1
    elif menu == "3":
        print(f"{drinks[2]}를 주문하셨습니다. 가격은 {price[2]}원입니다")
        total_price = total_price + price[2]
        amounts[2] = amounts[2] + 1
    elif menu == "4" :
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 멘에서 골라주세요.")

print(f"{drinks[0]} {price[0]}원 {amounts[0]}잔 {price[0] * amounts[0]}")
print(f"{drinks[1]} {price[1]}원 {amounts[1]}잔 {price[1] * amounts[1]}")
print(f"{drinks[2]} {price[2]}원 {amounts[2]}잔 {price[2] * amounts[2]}")
print(f"총 주문 금액 : {total_price}원")