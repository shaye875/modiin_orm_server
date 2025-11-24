from tables.report import *
from tables.ageint import *
from datetime import datetime
from tables.terorist import *
from get_reportes import *
while True:
    id_1 = input("what is your id:\n")
    id_1 = int(id_1)
    name = input("what is your name:\n")
    bool = true_agent(id_1,name)
    if bool == False:
        print("you not in the system")
        continue
    print("welcome")
    menu = int(input("what do you want to do\n1-add report\n2-get all reported\n3-get reported by id\n4-delete reported by id\n5-get by terrorist\n6-get terrorist dangers\n7-get terrorist super dangers\n8-get report by the word\n9-get table of terrorist\n10-exit"))
    if menu == 1:
       terrorist =  input("what is num of terrorist")
       level = input("what is level")
       report = input("write the report")
       add_report(id_1,int(terrorist), int(level), report)
    elif menu == 2:
        print(get_reports_by_id())
    elif menu == 3:
        id = int(input("which id?"))
        print(get_reports_by_id(id))
    elif menu == 4:
        id = input("which id?")
        del_report(id)
    elif menu == 5:
        terrorist = int(input("which id?"))
        print(get_by_terrorist(terrorist))
    elif menu == 6:
        dangerous_terrorist()
    elif menu == 7:
        super_dangerous_terrorist()
    elif menu == 8:
        word = input("which word?")
        print(get_report_by_report(word))
    elif menu == 9:
        print(get_terrorist())
    elif menu == 10:
        print("good by")
        break

