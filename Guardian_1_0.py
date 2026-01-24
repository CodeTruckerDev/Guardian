import time, os

### Add date to txt file ###
file = open("newFile.txt", "a")
file.write(time.strftime("%Y-%m-%d\n")) # "%Y-%m-%d %H:%M\n"
file.close()

### Read 3 last lines ###
file = open("newFile.txt", "r")
data = file.readlines()
if data[-1] == data[-2] == data[-3]:
    
    ### If they are equall shutdown in 1 minute ###
    os.system("\""+"shutdown /s /f /t 60"+"\"")
    
### If not equall shutdown in 61 minutes ###
else:
    os.system("\""+"shutdown /s /f /t 3660"+"\"")
file.close()
