import datetime
from time import sleep
from random import randint
a = datetime.datetime.today()
FILE = ""
with open('C:\\Users\\stasu\\Desktop\\status.dat', 'r') as f:
    FILE = f.read()
    f.close()

while True:
    with open('C:\\Users\\stasu\\Desktop\\status.dat', 'w') as f:
        f.write(FILE[:4]
                + str(a)[0:4] + str(a)[5:7] + str(a)[8:10] + str(a)[11:13] + str(a)[14:16] + str(a)[17:19] + FILE[18:50] #Change actual date
                + str(a)[0:4] + str(a)[5:7] + str(a)[8:10] + str(a)[11:13] + str(a)[14:16] + str(a)[17:19]  # Change Beginning_run_date
                + str(randint(2000000, 2500000)).rjust(10, "0") + FILE[74:84] #Change Actual_lineal_meters_mm
                + str(randint(100, 200)).ljust(6, "0") #Change Current_speed_mm_min
                + str(randint(100, 200)).ljust(6, "0") + FILE[96:120] #Average_speed_mm_min
                + str(randint(10000, 12000)).rjust(6, "0") # Actual_cuts_customer_1
                +FILE[126:])
        f.close()
    sleep(5)

