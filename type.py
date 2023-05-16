import pymysql

try:
    db = pymysql.connect(host='localhost', user='root', password='root', database='School')
    print("connect success")
except pymysql.Error as e:
    print('connect fail')
cur = db.cursor()
if not cur:
    print('fail')
else:
    print('success')


class Student():
    def __init__(self, id, nom, prenom, age, heure, psd):
        self.id = id
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.age = int(age)
        self.heure = int(heure)
        self.psd = psd
    def afficher(self):
        cur.execute("Select stu_id,stu_nom,stu_prenom,stu_age,stu_heure from Student  Where stu_id =  (%d)" % (self.id))
    def modifier(self):
        psd1 = int(input('Write your old password :'))
        psd2 = int(input('Write your new password:'))
        cur.execute("Select stu_psd from Student Where sut_id = (%d)" %(self.id))
        row1 = cur.fetchone()
        if row1[0] ==psd1:
            cur.execute("UPDATE  Student Set stu_psd =(%d) WHERE stu_psd = (%d)" % (psd2))
        else:
            print('votre password ne est correct.')
    def afficher_cour(self):
        cur.execute("Select * from Cour Where cour_student = ('%s')+('%s')" % (self.nom),(self.prenom))
        row1 = cur.fetchone()
        print(row1)
class Teacher():
    def __init__(self, id, nom, prenom, sexe, psd):
        self.psd = psd
        self.id = int(id)
        self.nom = str(nom)
        self.sexe = str(sexe)
        self.prenom = str(prenom)
    def afficher_cour(self):
        cur.execute("Select * from Cour Where cour_teacher = ('%s')+('%s')" % (self.nom),(self.prenom))
        row1 = cur.fetchone()
        print(row1)
    def modifier(self):
        psd1 = int(input('Write your old password:'))
        psd2 = int(input('Write your new password:'))
        cur.execute("Select tea_psd from Teacher Where tea_id = (%d)" %(self.id))
        row1 = cur.fetchone()
        if row1[0] ==psd1:
            cur.execute("UPDATE  Teacher Set tea_psd =(%d) WHERE tea_psd = (%d)" % (psd2))
        else:
            print('votre password ne est correct.')
    def ajouter_cour(self):
            id = int(input('Write id de eleve:'))
            dure = int(input('Write dure de cour:'))
            nom = str(input('Write name de cour:'))
            date = int(input('Write starttime(exemple:AAAAMMDD):'))
            time = int(input('Write starttime(exemple:HHMMSS):'))
            eleve = str(input('Write NOM+Prenom de eleve:'))
            prof = self.nom+self.prenom
            car = str(input('Write nom de car:'))
            cur.execute("INSERT INTO Cour VALUES (%d,'%s',%d,%d,%d,'%s','%s','%s')" % (id,nom,dure,date,time,eleve,prof,car))
            db.commit()
            print('ajouter finir')
    def ajouter_heure(self):
            id = int(input('Write id de eleve:'))
            dure = int(input('Write dure de cour:'))
            cur.execute("Select stu_dure from Student Where stu_id = (%d)" % (id))
            row1 = cur.fetchone()
            dure = dure + row1[0]
            cur.execute("UPDATE  Student Set stu_dure =(%d) WHERE stu_id = (%d)" % (dure,id))
class Monitor():
    def __init__(self, id, psd):
        self.id = id
        self.psd = psd

    def ajouter(self):
        choisir = str(input('Taper 1,2,3,4 pour ajouter eleve ou professeur ou voiture ou cour:'))
        if choisir == '1':
            id = int(input('Write id:'))
            nom = str(input('Write nom:'))
            prenom = str(input('Write prenom:'))
            age = int(input('Write age:'))
            sexe = str(input('write type of sexe M or F:'))
            psd = int(input('Write psd:'))
            heure = int('0')
            sql = "INSERT INTO Student VALUES (%d,'%s','%s',%d,'%s',%d,%d )" % (id,nom,prenom,age,sexe,psd,heure)
            cur.execute(sql)
            db.commit()
            print('ajouter finir')
        elif choisir == '2':
            id = int(input('Write id:'))
            nom = str(input('Write nom:'))
            prenom = str(input('Write prenom:'))
            psd = int(input('Write psd:'))
            sql = "INSERT INTO Teacher VALUES (%d,'%s','%s',%d)" % (id,nom,prenom,psd)
            cur.execute(sql)
            db.commit()
            print('ajouter finir')
        elif choisir == '3':
            id = int(input('Write id:'))
            nom = str(input('Write nom:'))
            cur.execute("INSERT INTO Car VALUES (%d,'%s')" % (id,nom))
            db.commit()
            print('ajouter finir')
        elif choisir == '4':
            id = int(input('Write id:'))
            nom = str(input('Write name de cour:'))
            dure = int(input('Write dure:'))
            date = int(input('Write starttime(exemple:AAAAMMDD):'))
            time = int(input('Write starttime(exemple:HHMMSS):'))
            eleve = str(input('Write NOM+Prenom de eleve:'))
            prof = str(input('Write NOM+Prenom de prof:'))
            car = str(input('Write nom de car:'))
            cur.execute("INSERT INTO Cour VALUES (%d,'%s',%d,%d,%d,'%s','%s','%s')" % (id,nom,dure,date,time,eleve,prof,car))
            db.commit()
            print('ajouter finir')
        else:
            print('Je comprend votre choisi')

    def afficher(self):
        choisir = str(input('Taper 1,2,3 pour afficher eleve ou professeur ou voiture:'))
        if choisir == '1':
            cur.execute('Select * from Student')
            print(cur.fetchall())
        elif choisir == '2':
            cur.execute('Select * from Teacher')
            print(cur.fetchall())

        elif choisir == '3':
            cur.execute('Select * from Car')
            print(cur.fetchall())
        else:
            print('Comprend pas votre choisi')
    def supprimer(self):
        choisir = str(input('Taper 1,2,3,4 pour supprimer eleve ou professeur ou voiture ou cour:'))
        if choisir == '1':
            nom = str(input('nom de eleve pour supprimer:'))
            prenom = str(input('prenom de eleve pour supprimer:'))
            cur.execute("DELETE from Student Where stu_nom = ('%s') AND stu_prenom = ('%s') "% (nom,prenom))
        elif choisir == '2':
            nom = str(input('nom de professeur pour supprimer:'))
            prenom = str(input('prenom de professeur pour supprimer:'))
            cur.execute("DELETE from Teacher Where tea_nom = ('%s') AND tea_prenom = ('%s') "% (nom,prenom))
        elif choisir == '3':
            nom = str(input('nom de voiture pour supprimer:'))
            cur.execute("DELETE from Car Where car_nom = ('%s') "% (nom))
        elif choisir =='4':
            nom = str(input('nom de cour pour supprimer:'))
            date = str(input('La date pour supprimer Exemple(2023-05-15):'))
            time = str(input('Quelle heure pour supprimer Exemple(15:30:00):'))
            cur.execute("DELETE from Cour Where cour_name = ('%s') AND cour_date=(%d) AND cour_time=(%d)  " % (nom,date,time))

    def modifier(self):
        choisir = str(input('Taper 1,2,3,4 pour modifier eleve ou professeur ou voiture ou cour:'))
        if choisir == '1':
            choose = str(input('Taper 1,2,3,4 pour modifier name ou age ou sexe  ou password :'))
            if choose == '1':
                nom1 = str(input('nom de eleve pour modifier:'))
                prenom1 = str(input('prenom de eleve pour modifier:'))
                nom2 = str(input('renouvelle nom de eleve:'))
                prenom2 = str(input('renouvelle prenom de eleve :'))
                cur.execute("UPDATE  Student Set stu_nom =('%s'),stu_prenom = ('%s') Where stu_nom = ('%s') AND stu_prenom = ('%s') " % (nom2, prenom2,nom1,prenom1))
            if choose == '2':
                nom = str(input('nom de eleve pour modifier:'))
                prenom = str(input('prenom de eleve pour modifier:'))
                age = str(input('renouvelle age de eleve:'))
                cur.execute("UPDATE  Student Set stu_age =('%s') Where stu_nom = ('%s') AND stu_prenom = ('%s') " % (age,nom, prenom))
            if choose == '3':
                nom = str(input('nom de eleve pour modifier:'))
                prenom = str(input('prenom de eleve pour modifier:'))
                sexe = str(input('renouvelle sexe de eleve:'))
                cur.execute("UPDATE  Student Set stu_sexe =('%s') Where stu_nom = ('%s') AND stu_prenom = ('%s') " % (sexe, nom, prenom))
            if choose == '4':
                nom = str(input('nom de eleve pour modifier:'))
                prenom = str(input('prenom de eleve pour modifier:'))
                psd = int(input('renouvelle password de eleve:'))
                cur.execute("UPDATE  Student Set stu_psd =(%d) Where stu_nom = ('%s') AND stu_prenom = ('%s') " % (psd, nom, prenom))
        if choisir == '2':
            choose = str(input('Taper 1,2 pour modifier name ou password:'))
            if choose == '1':
                if choose == '1':
                    nom1 = str(input('nom de professeur pour modifier:'))
                    prenom1 = str(input('prenom de professeur pour modifier:'))
                    nom2 = str(input('renouvelle nom de professeur:'))
                    prenom2 = str(input('renouvelle prenom de professeur :'))
                    cur.execute("UPDATE  Teacher Set tea_nom =('%s'),tea_prenom = ('%s') Where tea_nom = ('%s') AND tea_prenom = ('%s') " % (nom2, prenom2, nom1, prenom1))
                if choose == '2':
                    nom = str(input('nom de professeur pour modifier:'))
                    prenom = str(input('prenom de professeur pour modifier:'))
                    psd = int(input('renouvelle password de professeur:'))
                    cur.execute("UPDATE  Teacher Set tea_psd =(%d) Where tea_nom = ('%s') AND tea_prenom = ('%s') " % (psd, nom, prenom))
        if choisir == '3':
            name1 = str(input('nom de voiture pour modifier:'))
            name2 = str(input('renouvelle nom de voiture :'))
            cur.execute("UPDATE  Car Set car_nom =('%s') Where car_nom = ('%s') " % (name2,name1))
        if choisir == '4':
            choose = str(input('Taper 1,2,3,4,5,6,7 pour modifier name ou eleve ou professeur ou voiture ou date ou time ou dure de cour:'))
            if choose == '1':
                name1 = str(input('nom de cour pour modifier:'))
                date = int(input('Write date de ce cour(exemple:AAAAMMDD):'))
                time = int(input('Write time de ce cour(exemple:HHMMSS):'))
                name2 = str(input('renouvelle nom de cour:'))
                cur.execute("UPDATE  Cour Set cour_name =('%s') Where cour_name = ('%s') AND cour_date = (%d) AND cour_time = (%d) " % (name2, name1,date,time))
            if choose == '2':
                name = str(input('nom de cour pour modifier:'))
                date = int(input('Write date de ce cour(exemple:AAAAMMDD):'))
                time = int(input('Write time de ce cour(exemple:HHMMSS):'))
                nom = str(input('renouvelle nom de eleve:'))
                prenom = str(input('renouvelle prenom de eleve:'))
                cur.execute("UPDATE  Cour Set cour_student =('%s') Where cour_name = ('%s') AND cour_date = (%d) AND cour_time = (%d) " % (nom+' '+prenom, name, date, time))
            if choose == '3':
                name = str(input('nom de cour pour modifier:'))
                date = int(input('Write date de ce cour(exemple:AAAAMMDD):'))
                time = int(input('Write time de ce cour(exemple:HHMMSS):'))
                nom = str(input('renouvelle nom de professeur:'))
                prenom = str(input('renouvelle prenom de professeur:'))
                cur.execute("UPDATE  Cour Set cour_teacher =('%s') Where cour_name = ('%s') AND cour_date = (%d) AND cour_time = (%d) " % (nom +' '+ prenom, name, date, time))
            if choose == '4':
                name = str(input('nom de cour pour modifier:'))
                date = int(input('Write date de ce cour(exemple:AAAAMMDD):'))
                time = int(input('Write time de ce cour(exemple:HHMMSS):'))
                nom = str(input('renouvelle nom de voiture:'))
                cur.execute("UPDATE  Cour Set cour_voiture =('%s') Where cour_name = ('%s') AND cour_date = (%d) AND cour_time = (%d) " % (nom, name, date, time))
            if choose == '5':
                name = str(input('nom de cour pour modifier:'))
                date1 = int(input('Write date de ce cour(exemple:AAAAMMDD):'))
                time = int(input('Write time de ce cour(exemple:HHMMSS):'))
                date2 = str(input('Renouvelle date de ce cour(exemple:AAAAMMDD):'))
                cur.execute("UPDATE  Cour Set cour_date =('%s') Where cour_name = ('%s') AND cour_date = (%d) AND cour_time = (%d) " % (date2, name, date1, time))
            if choose == '6':
                name = str(input('nom de cour pour modifier:'))
                date = int(input('Write date de ce cour(exemple:AAAAMMDD):'))
                time1 = int(input('Write time de ce cour(exemple:HHMMSS):'))
                time2 = str(input('Renouvelle time de ce cour(exemple:HHMMSS):'))
                cur.execute("UPDATE  Cour Set cour_time =('%s') Where cour_name = ('%s') AND cour_date = (%d) AND cour_time = (%d) " % (time2, name, date, time1))
            if choose == '7':
                name = str(input('nom de cour pour modifier:'))
                date = int(input('Write date de ce cour(exemple:AAAAMMDD):'))
                time = int(input('Write time de ce cour(exemple:HHMMSS):'))
                dure = int(input('Renouvelle dure de ce cour:'))
                cur.execute("UPDATE  Cour Set cour_dure =('%s') Where cour_name = ('%s') AND cour_date = (%d) AND cour_time = (%d) " % (dure, name, date, time))
monitor1 = Monitor(1234, 1234)

monitor1.modifier()
monitor1.afficher()

