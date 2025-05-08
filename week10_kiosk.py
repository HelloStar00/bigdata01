
import kiosk as k;

if __name__ == "__main__":
    while True:
        try:
            menu = int(input(k.display_menu()))
            if len(k.drinks) >= menu >= 1:
                k.order_process(int(menu) - 1)
            elif menu == len(k.drinks) + 1:
                print("주문을 종료합니다")
                break
            else:
                print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요.")
        except ValueError:
            print(f"문자를 입력할 수 없습니다. 숫자를 입력해주세요.")
    k.print_receipt()

"""
    어플라이 디스카운터(변수)를 만들거임
    만원을 넘으면 10% 할인해주는 것
"""