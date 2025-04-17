# 1) 아아 : 2000원 2) 라떼 : 2500원
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스"]
price = [1500, 2500, 4000]
amounts = [0, 0, 0]
total_price = 0

def order_process(idx):
    """
    주문처리 함수 1) 주문 디스플레이 2) 총 주문 금액 누산 3) 주문 품목 수량
    return : 없음
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {price[idx]}원입니다.")
    total_price = total_price + price[idx]
    amounts[idx] = amounts[idx] + 1

menu_texts = ""
for j in range(len(drinks)) :
    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {price[j]}원 "
menu_texts = menu_texts + f"{len(drinks)+1}) 주문 종료 : "

while True :
    menu = input(menu_texts)
    if menu == "1" :
        order_process(int(menu) - 1)
    elif menu == "2":
        order_process(int(menu) - 1)
    elif menu == "3":
        order_process(int(menu) - 1)
    elif menu == "4" :
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 멘에서 골라주세요.")

print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i] > 0 :
        print(f"{drinks[i]} {price[i]}원 {amounts[i]}잔 {price[i] * amounts[i]}원")
print(f"총 주문 금액 : {total_price}원")