import kiosk as k

while True :
    try :
        menu = int(input(k.display_menu()))
        if len(k.drinks) >= menu >= 1:
            k.order_process(int(menu) - 1)
        elif menu == len(k.drinks) + 1 :
            print("주문을 종료합니다")
            break
        else:
            print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요.")
    except ValueError :
        print(f"문자를 입력할 수 없습니다. 숫자를 입력해주세요.")

print(f"\n총 주문 금액 : {k.total_price}원\n")
k.print_receipt()


"""
    모듈
git reset
    파일로 분리해서 해 볼거임
    왜 분리하냐 >> 유지 보수나 관리가 쉽기 때문에
    k.py
    모듈로 만드는 파일은 함수나 클래스를 가짐
    함수 3개를 옯길거야 k.py로
    
    1. k.py 생성
    2. def 함수 모두 k로 옯김
    3. 선언한 전역 변수로 k.py로 옯김
    >> week09_k.py에는 (C++이라고 할 때) main함수로만 남음
    4. k.py를 import함
    5. 변수 이름 앞에다가 'k.'을 붙임
    ** 코드를 수정한 후에는 반드시 실행 해보기**
    6. 'k.'을 줄여서 쓰기 위해 as를 사용함
        ㄴ import k.py as k
"""