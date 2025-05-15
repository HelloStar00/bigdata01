# 1) 아아 : 2000원 2) 라떼 : 2500원
import kiosk

drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
price = [1500, 2500, 4000, 4200]
total_price = 0
amounts = [0] * len(drinks)

# 파이썬에서는 대문자와 언더바를 통해 상수 선언
# 할인 적용 정책
DISCOUNT_THRESHOLD = 10000  # 할인이 적용 되는 임계값 (임계값 이상이면 할인 적용)
DISCOUNT_RATE = 0.1         # 할인율
# 협업할 때 변수, 상수 이름이 중요함

def run() -> None:
    """
    키오스크 실행(구동) 함수
    :return: None
    """
    while True:
        try:
            menu = int(input(kiosk.display_menu()))
            if len(kiosk.drinks) >= menu >= 1:
                kiosk.order_process(menu - 1)
            elif menu == len(kiosk.drinks) + 1 :
                print("주문을 종료합니다.")
                break
            else:
                print(f"{menu}번 메뉴는 존재하지 않습니다.")
        except ValueError:
            print(f"문자를 입력할 수 없습니다. 숫자를 입력해 주세요.")

def apply_discount(price:int) -> float :
    """
    총 금액이 특정 금액(인계값)을 넘어서면 할인율 적용 함수
    :param price: 할인 전 총 금액
    :return: 할인이 적용된 금액 또는 할인이 적용되지 않은 금액
    """
    if price >= DISCOUNT_THRESHOLD:
        return price * (1 - DISCOUNT_RATE)
    return price

def print_ticket_number() -> None :
    """
    주문 번호표 처리 기능 함수
    :return: 번호

    함수 이름 원래 get_ticket_number 였는데
    get은 원래 리턴을 받을 때 주로 쓰는 거라서
    return값이 없고 print만 있으니
    이름을 print_ticket_number로 바꿈
    """
    try :
        with open("ticket.txt", "r") as fp:
            number = int(fp.read())
    except FileNotFoundError :
        number =0

    number = number + 1

    with open("ticket.txt", "w") as fp :
        fp.write(str(number))

    print(f"번호표 : {number}")
    # return number

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

    discounted_price = apply_discount(total_price)
    discount = total_price - discounted_price

    print(f"\n할인 전 총 주문 금액 : {total_price}원")
    if discount > 0 :
        print(f"할인 금액 : {discount}원 {DISCOUNT_RATE * 100}%") # 영수증에 할인율 추가
        print(f"할인 적용 후 지불하실 총 금액 : {discounted_price}원")
    else:
        print(f"할인이 적용되지 않았습니다. \n지불하실 총 금액은 {total_price}원 입니다.")


def test() -> None :
    pass
    # 앞으로 넣을 키오스크 기능