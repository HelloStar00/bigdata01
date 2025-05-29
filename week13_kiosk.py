#open api : wttr.in (weather info)
import kiosk as k
import requests

if __name__ == "__main__":

    url = f"http://wttr.in/seoul?format=%C+%t&lang=ko"
    response = requests.get(url)
    print(response.text.strip())
    k.run()
    k.print_receipt()
    k.print_ticket_number()
