import request, os

today = requests.get("http://just-the-time.appspot.com").text.split()[0] + "\n"
with open("newFile.txt", "a+") as file:
    file.seek(0)
    file.write(today)
    data = file.readlines()[-1:-3:-1]
    if data[0] == data[1] == today:
        os.system('"' + "shutdown /s /f /t 60" + '"')
    else:
        os.system('"' + "shutdown /s /f /t 3660" + '"')
