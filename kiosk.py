# 1) 아아 : 2000원 2) 라떼 : 2500원
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
price = [1500, 2500, 4000, 4200]
total_price = 0
amounts = [0] * len(drinks)

def apply_discount(price:int) -> float :
    """
    총 금액이 특정 금액(인계값)을 넘어서면 할인율 적용 함수
    :param price: 할인 전 총 금액
    :return: 할인이 적용된 금액 또는 할인이 적용되지 않은 금액
    """
    pass

def order_process(idx : int) -> None:   # type hint
    """
    주문처리 함수 1) 주문 디스플레이 2) 총 주문 금액 누산 3) 주문 품목 수량 업데이트
    :param idx: 고객이 선택한 메뉴 - 1 (인덱스, 정수)
    return : 없음
    """
    global total_price
    print(f"{drinks[idx]}를 주문하셨습니다. 가격은 {price[idx]}원입니다.")
    total_price = total_price + price[idx]
    amounts[idx] = amounts[idx] + 1

def display_menu() -> str:  # type hint
    """
    음료 선택 메뉴 디스플레이 함수
    :return: 음료 메뉴 및 주문 종료 문자열
    """
    menu_texts = "".join([f"{j+1}) {drinks[j]} {price[j]}원\n "for j in range(len(drinks))])
    menu_texts = menu_texts + f"{len(drinks)+1}) 주문 종료 : "
    return menu_texts

def print_receipt() -> None:    # type hint
    """
    영수증 출력 기능
    :return: 없음
    """
    print(f"{'상품명':^20}{'단가':^6}{'수량':^6}{'금액' :^6}")
    for i in range(len(drinks)):
        if amounts[i] > 0:
            print(f"{drinks[i]:^20}{price[i]:^6}{amounts[i]:^6}{price[i] * amounts[i]:^6}")

def test() -> None :
    pass
    # 앞으로 넣을 키오스크 기능