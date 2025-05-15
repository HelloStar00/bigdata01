import kiosk as k

if __name__ == "__main__" :
    k.run()
    k.print_receipt()
    k.print_ticket_number()
    # get_ticket_number()를 여기서 하는게 아니라 get_ticket_number()안에서 하기
    
    # 스타벅스 영수증과 비교했을 때 현재 날짜 시간과 주소 등이 없어 추가해 줄 것임

    """ [데이터 베이스 연결]
    
        sqllite3 다운 받아서 bigdata01 폴더에 넣음
        이건 git 폴더에 안 올릴 거임
        .ignore 에 *.exe 추가하기
        
        터미널에
        ./sqlite3 temp.db # 임시 데이터베이스
        입력
        
        테이블 만들거임
        create table ticket(테이블 이름)  (id integer primary key autoincrement, number integer not null);
        
        .tables >> 테이블들을 보여주는 것
        .schema >> 지금까지의 스키마를 보여줌
        
        테이블의 값 넣기
        insert into ticket (number) values (100); 
        
        .head on  >> 반드시 줄바꿈 필요
        select ~~ >> 구분과 함께 목록을 보여줌
        
        테이블 삭제
        drop table ticket;
        
        db 종료
        .quit
        
        .ignore에 *.db를 추가해서 git에서 무시하게 만들기 
        
        >> temp.py에서 계속
    """