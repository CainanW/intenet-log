import subprocess
import datetime
import time
import os.path




while(1):

    file = open('internetdata.txt', 'a')

    
    output = subprocess.call(['ping', 'google.com'], shell=True)

    print(output)

    if (output == 0):
        file.write(str(datetime.datetime.now())+ " " +str(output)+" Internet is working!\n")
    else:
        file.write(str(datetime.datetime.now())+ " " +str(output)+" Internet is NOT working!\n")

    file.close()
    
    time.sleep(300)
