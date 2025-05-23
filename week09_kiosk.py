# import kiosk as k
# from kiosk import * #이건 충돌 관련한 문제를 조심 해야 한다.
from kiosk import drinks, display_menu, order_process, print_receipt

while True :
    try :
        menu = int(input(display_menu()))
        if len(drinks) >= menu >= 1:
            order_process(int(menu) - 1)
        elif menu == len(drinks) + 1 :
            print("주문을 종료합니다")
            break
        else:
            print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요.")
    except ValueError :
        print(f"문자를 입력할 수 없습니다. 숫자를 입력해주세요.")
print_receipt()

# total_price
# test()


"""
    모듈
    git reset
    파일로 분리해서 해 볼거임
    왜 분리하냐 >> 유지 보수나 관리가 쉽기 때문에
    k.py
    모듈로 만드는 파일은 함수나 클래스를 가짐
    함수 3개를 옯길거야 k.py로
    
    1. kiosk.py 생성
    
    2. def 함수 모두 kiosk.py 옯김
    
    3. 선언한 전역 변수로 kiosk.py로 옯김
    >> week09_kiosk.py에는 (C++이라고 할 때) main함수만 남음
    
    4. kiosk.py를 import 함
        ㄴ import kiosk
        
    5. 변수 이름 앞에 'kiosk.'을 붙임
        ㄴ ex) kiosk.drinks
        
    ** 코드를 수정한 후에는 반드시 실행 해보기**
    
    6. 'kiosk.'을 줄여서 쓰기 위해 as를 사용함
        ㄴ import k.py as k / k.drinks
        
    7. k. 도 쓰지 않기 위해서는 아래와 같이 작성
        ㄴ from kiosk import *
        ㄴ 이걸 사용하면 k.를 안 써도 됨
        ㄴ 단점 : 아직 완성되지 않은 기능까지 실행됨
        
    8. from kiosk import drinks, display_menu, order_process, print_receipt
        ㄴ 선택한 함수만 사용할 수 있음
        ㄴ 사실 from kiosk import * 는 잘 안 씀
"""