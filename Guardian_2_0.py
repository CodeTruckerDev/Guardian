import request 
import os
import time

def guardian():
    today = requests.get("http://just-the-time.appspot.com").text.split()[0] + "\n" # dzisiejszą datę pobieram z zewnątrz
    with open("newFile.txt", "a+") as file:
        file.seek(0)
        file.write(today)
        data = file.readlines()[-1:-3:-1]
        if data[0] == data[1] == today:
            os.system('"' + "shutdown /s /f /t 60" + '"')
        else:
            os.system('"' + "shutdown /s /f /t 3660" + '"')

def sprawdz_polaczenie():
    """Sprawdza czy jest połączenie z internetem"""
    try:
        requests.get('http://www.google.com', timeout=3)
        return True
    except requests.exceptions.RequestException:
        return False

while True:
    if sprawdz_polaczenie():
        guardian()
        break
    else:
        time.sleep(5) # przy braku połączenia czekam 5 sekund
