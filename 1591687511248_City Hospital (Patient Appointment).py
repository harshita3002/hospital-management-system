import mysql.connector as sql
con=sqltor.connect(host="localhost",user="root",password="hello")
cur=con.cursor()
cur.execute("create table if not exists appt"
            "aadharno char(12) primary key,"
            "name char(20),"
            "age int(10),"
            "gender char(1),"
            "phone char(10),"
            "bloodgroup char(3))"
print("""  
  
               ___       ___   ___            ___     _____ ___       ___  _____ _____
     |      | |    |    |   | |   | |\    /| |          |  |   |     |   |   |     |   |   |
     |  /\  | |__  |    |     |   | | \  / | |__        |  |   |     |       |     |   |___|
     | /  \ | |    |    |     |   | |  \/  | |          |  |   |     |       |     |       |
     |/    \| |___ |___ |___| |___| |      | |___       |  |___|     |___| __|__   |    ___|
   _________________________________________________  __________    _________________________
                         
                            ___   ___   ___  _____  _____  ____    
                     |   | |   | |     |   |   |      |   |    |  |
                     |___| |   | |___  |___|   |      |   |____|  |
                     |   | |   |     | |       |      |   |    |  |
                     |   | |___|  ___| |     __|__    |   |    |  |____
                    ____________________________________________________                
          """)
def data():
        while True:
            aadharno=input("Adhaar no.:")
            if len(aadharno)==12 :
                break
            else:
                print("12 digits required!")
               
        name=input("Patient name:")
        while True:
            age=int(input("Age:"))
        
        while True:
            gen=input("Gender F/M:")
            if gen==("M") or gen==("F"):
                break
            else:
                print("F/M only!")
        
        while True:
            phn=input("Phone no.:")
            if len(ph)==10 :
                break
            else:
                print("10 digits required!")
        while True:
            bloodgroup=input("""Blood group(A+,B+,O+,AB+,A-,B-,O-,AB-):-""")
            if bloodgroup==("A+") or bloodgroup==("B+") or bloodgroup==("o+") or bloodgroup==("AB+") or bloodgroup==("A-") or bloodgroup==("B-") or bloodgroup==("O-") or bloodgroup==("AB-"):
                break
            else:
                print("Enter valid blood group!")
        cur.execute("insert into appt(aadharno,name,age,gender,phone,bloodgroup) values(%s,%s,%s,%s,%s,%s)",(idn,name,age,gen,ph,bg,))
        con.commit()
        print(" ")
        print("""   
         YOU HAVE BEEN REGISTERED
             """)
          
        print("""
       
        Your details are as follows:-
       
        """)
        cur.execute("select * from appt where aadharno=(%s);",(aadharno,))
        d=cur.fetchall()
        for i in d:
            print("""     Aadhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
        return("")
       

