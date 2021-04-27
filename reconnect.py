import os
import subprocess
import time
def mapDrive(drive, networkPath, user, password, force=1):
    if (os.path.exists(drive)):
        if force:
            try:
                subprocess.call(r'net use '+drive+ ' /del /Y', shell=True,stdout=subprocess.DEVNULL)
            except Exception as e:
                print(e)
                return -1
        else:
            return -1
    else:
        print ("...")
    if (os.path.exists(networkPath)):
        print ("...")
        try:
            subprocess.call(r'net use '+drive+ ' \\\\Konstruktion\\Solidworks', shell=True,stdout=subprocess.DEVNULL)
        except Exception as E:
            print(E)
            return -1

        return "Success"
    else:
        return "Fail"



print("Prøver at mappe drevet (Prøver 8 gange i alt)")

result = mapDrive("P:","\\\\Konstruktion\\Solidworks", "","")
if result == "Fail":
    for x in range(1,8):
        print("Fejlede, prøver igen...")
        print("Prøver forsøg "+str(x)+ " af 8")
        retry = mapDrive("P:","\\\\Konstruktion\\Solidworks", "","") 
        if retry == "Success":
            print("Alles gut, drevet er nu mapped og klar til brug") 
            time.sleep(3)
            sys.exit()
        time.sleep(5)
        if x == 8:
            print("Kunne ikke connect drevet, prøv at genstarte PC")
            time.sleep(1000)
            sys.exit()
if result == "Success":
    print("SUCCESS, drevet er nu mapped og klar til brug") 
    time.sleep(3)
    sys.exit()

