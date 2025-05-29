#open api : wttr.in (weather info)
import kiosk as k
import requests

if __name__ == "__main__":

    # url = f"http://wttr.in/seoul?format=%C+%t&lang=ko"
    url = f"http://naver.com/kim" # 404 page not found
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text.strip())
    else:
        print(f"상태코드 : {response.status_code}")
    k.run()
    k.print_receipt()
    k.print_ticket_number()
