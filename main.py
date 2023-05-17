import pymysql
import type
try:
    db = pymysql.connect(host='localhost', user='root', password='root', database='School')
    print("connect success")
except pymysql.Error as e:
    print('connect fail')
cur = db.cursor()
if not cur:
    print('fail')
else:
    print('date get success')
def start():
    restart = True
    while restart == True:
        print('---Welcome to auto-school system---')
        id = int(input('Please write your id:'))
        password = int(input('Please write your password:'))
        cur.execute("Select stu_id,stu_psd from Student ")
        row1 = cur.fetchall()
        cur.execute("Select tea_id,tea_psd from Teacher ")
        row2 = cur.fetchall()
        cur.execute("Select DISTINCT mon_id,mon_psd from Monitor ")
        row3 = cur.fetchall()
        for i in row1:
            if i[0] == id and i[1] == password:
                student1 = type.Student(id,password)
                b = True
                while b== True:
                    print('------Welcome,select your option------')
                    print('Select 1 pour afficher ton information')
                    print('Select 2 pour modifier ta password')
                    print('Select 3 pour afficher ton cour')
                    print('Select 4 pour quitter')
                    a = int(input('Your option:'))
                    if a == 1 :
                        student1.afficher()
                    elif a == 2:
                        student1.modifier()
                    elif a == 3:
                        student1.afficher_cour()
                    elif a == 4:
                        continue
                    else:
                        print('Je comprend votre option')
        for i in row2:
            if i[0] == id and i[1] == password:
                teacher1 = type.Teacher(id,password)
                b = True
                while b== True:
                    print('------Welcome,select your option------')
                    print('Select 1 pour afficher ton cour')
                    print('Select 2 pour modifier ta password')
                    print('Select 3 pour ajouter cour')
                    print('Select 4 pour ajouter heure')
                    print('Select 5 pour quitter')
                    a = int(input('Your option:'))
                    if a == 1 :
                        teacher1.afficher_cour()
                    elif a == 2:
                        teacher1.modifier()
                    elif a == 3:
                        teacher1.ajouter_cour()
                    elif a == 4:
                        teacher1.ajouter_heure()
                    elif a ==5:
                        continue
                    else:
                        print('Je comprend pas votre option')
        for i in row3:
            if i[0] == id and i[1] == password:
                monitor1 = type.Monitor(id,password)
                b = True
                while b== True:
                    print('------Welcome,select your option------')
                    print('Select 1 pour ajouter')
                    print('Select 2 pour afficher')
                    print('Select 3 pour supprimer')
                    print('Select 4 pour modifier')
                    print('Select 5 pour quitter')
                    a = int(input('Your option:'))
                    if a == 1 :
                        monitor1.ajouter()
                    elif a == 2:
                        monitor1.afficher()
                    elif a == 3:
                        monitor1.supprimer()
                    elif a == 4:
                        monitor1.modifier()
                    elif a ==5:
                        continue
                    else:
                        print('Je comprend pas votre option')

start()