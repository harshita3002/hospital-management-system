
import mysql.connector as sqltor
con=sqltor.connect(host="localhost",user="root",password="dps@123")
cur=con.cursor()

cur = con.cursor(buffered=True) 

cur.execute("create database if not exists hello")

cur.execute("use hello")

cur.execute("create table if not exists appt"
            "("
            "idno char(12) primary key,"
            "name char(20),"
            "age int(10),"
            "gender char(1),"
            "phone char(10),"
            "bg char(3))")


                                
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

while True:
 print(""" 
      
    
        
        _______________                _______________                ____________
        |             |                |             |                |          |
        | 1. PATIENT  |                | 2. DOCTOR   |                | 3. EXIT  |
        |_____________|                |_____________|                |__________|
        
         
        
        """)
 e=input("||  SELECT || :-")
 
 if e=="1" :
     
  def dat():
        while True:
            idn=input("Adhaar no.:")
            if len(idn)==12 :
                break
            else:
                print(" ~!~!~!~~12 digits required~~!~!~!~")
               
        name=input("Patient name:")
        while True:
            age=int(input("Age:"))
            if type(age)!=int:
                print("~!~!~!~~digits required~~!~!~!~")
            else:
                break

        
        while True:
            gen=input("Gender M/F:")
            if gen==("M") or gen==("F"):
                break
            else:
                print("~!~!~!~~ M\F only ~~!~!~!~")
        
        while True:
            ph=input("Phone no.:")
            if len(ph)==10 :
                break
            else:
                print("~!~!~!~~10 digits required~~!~!~!~")
        while True:
            bg=input("""Blood group(A+,B+,O+,AB+,A-,B-,O-,AB-):-""")
            if bg==("A+") or bg==("B+") or bg==("o+") or bg==("AB+") or bg==("A-") or bg==("B-") or bg==("O-") or bg==("AB-"):
                break
            else:
                print("~!~!~!~~ Enter valid value ~~!~!~!~")
        cur.execute("insert into appt(idno,name,age,gender,phone,bg) values(%s,%s,%s,%s,%s,%s)",(idn,name,age,gen,ph,bg,))
        con.commit()
        print(" ")
        print("""   
          __________________________        
          |                        |
          |YOU HAVE BEEN REGISTERED| 
          |________________________|     
             """)
          
        print("""
        _______________________________ 
        |                             |
        |Your details are as follows:-|
        |_____________________________| 
        
        """)
        cur.execute("select * from appt where idno=(%s);",(idn,))
        d=cur.fetchall()
        for i in d:
            print("""     Adhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
        return("")
       


  def name():
        adr=int(input('ENTER YOUR ADHAAR NO:'))
        cur.execute('select * from appt where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     Adhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW NAME:-')
            cur.execute('update appt set name=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from appt where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     Adhaar no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")
        
               
    

  def age():
        adr=int(input('ENTER YOUR ADHAAR NO:'))
        cur.execute('select * from appt where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     Adhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW AGE:-')
            cur.execute('update appt set age=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from appt where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     Adhaar no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")
    
  def gen():
        adr=int(input('ENTER YOUR ADHAAR NO:'))
        cur.execute('select * from appt where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     Adhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW GENDER:-')
            cur.execute('update appt set gender=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from appt where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     Adhaar no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")         


  def ph():
        adr=int(input('ENTER YOUR ADHAAR NO:'))
        cur.execute('select * from appt where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     Adhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW PHONE NO:-')
            cur.execute('update appt set phone=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from appt where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     Adhaar no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("")


  def bg():
        adr=int(input('ENTER YOUR ADHAAR NO:'))
        cur.execute('select * from appt where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
            
        if len(a)!=1:
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:
            print('')
            print('''
            ------------------------    
            | YOUR OLD DETAILS ARE |
            ------------------------
            ''')
            
            print("")
            print("""     Adhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
            n=input('ENTER NEW BLOOD GROUP:-')
            cur.execute('update appt set bg=(%s) where idno=(%s);',(n,adr,))
            con.commit()
            cur.execute('select * from appt where idno=(%s)',(adr,))
            dat=cur.fetchall()
            for row in dat:
                print('')
                print('''
           ------------------------      
           | YOU NEW DETAILS ARE  |
           ------------------------      
                ''')
                print('')                
                print("""     Adhaar no.:-""",row[0])
                print('''     Name:-''',row[1])
                print('''     Age:-''',row[2])
                print('''     Gender:-''',row[3])
                print('''     Phone:-''',row[4])
                print('''     Bloodgroup:-''',row[5])
                con.commit()
        return("") 



  def ret():
        adr=int(input('Enter Adhaar no:'))
        cur.execute('select * from appt where idno=(%s)',(adr,))
        dat=cur.fetchall()
        a=[]
        for i in dat:
            a.append(i)
        if len(a)!=1:
            print('')
            print('~!~!~!~!~~NO DATA FOUND~~!~!~!~!~')
            
        else:

               while True:
                 print('''
      _______________________     
      |                     |
      |SELECT DEPARTMENT:-  |
      |                     |
      |1.Cardiologist       |
      |2.Rheumatologist     |
      |3.Psychitrist        |
      |4.Neurologist        |
      |5.Otolaryngonologist |
      |6.MI Room            |
      |7.Back               |
      |_____________________|
                 ''')
                
                 x=int(input("Enter choice:-"))
                
                 if x==1:
                    i=("Dr. Varun \nRoom no:- 201")
                    j=("Dr. Hrithik \nRoom no:- 202")
                    q=(i,j)
                    h=rd.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"\nDate:-",datetime.date.today() + datetime.timedelta(days=3))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                 elif x==2:
                    i=("Dr. Sidharth \nRoom no. 207")
                    j=("Dr. Abhishek \nRoom no. 208")
                    q=(i,j)
                    h=rd.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=5))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
               
                 elif x==3:
                    i=("Dr. Salman \nRoom no. 203")
                    j=("Dr. Shahrukh \nRoom no. 204")
                    q=(i,j)
                    h=rd.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=3))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                 elif x==4:
                    i=("Dr. Ajay, \nRoom no. 209")
                    j=("Dr. Ranveer \nRoom no. 200")
                    q=(i,j)
                    h=rd.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=6))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                 elif x==5:
                    i=("Dr. Akshay \nRoom no. 205")
                    j=("Dr. Amir \nRoom no. 206")
                    q=(i,j)
                    h=rd.choice(q)
                    print(' ')
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=4))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-:",o)
                    break
                 elif x==6:
                    i=("Dr. Irfan \nRoom no. 001")
                    j=("Dr. John \nRoom no. 002")
                    k=("Dr. Sanjay \nRoom no. 003")
                    l=("Dr. Shahid \nRoom no. 004")
                    q=(i,j,k,l)
                    h=rd.choice(q)
                    print(" ")
                    print("Your appointment is fixed with",h,"Date:-",datetime.date.today() + datetime.timedelta(days=1))
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                
                 elif x==7:
                    break
                 else:
                  print("~!~!~!~WRONG OPTION PLEASE ENTER VALID VALUE~!~!~!~")
                  
     
        return(" ")
            
                
    
  l={"NAME OF DOCTOR":["Dr. Varun","Dr. Hrithik","Dr. Salman","Dr. Shahrukh","Dr. Akshay","Dr. Amir","Dr. Sidharth","Dr. Abhishek","Dr. Ajay",
                     "Dr. Ranveer",'Dr. Irfan','Dr. John','Dr. Sanjay','Dr. Shahid'],
   "DEPARTMENT":["Cardiologist","Cardiologist","Psychiatrist","Psychiatrist","Opthamologist","Opthamologist","Rheumatologist","Rheumatologist","Neurologist",
                 "Neurologist",'MI room','MI room','MI room','MI room'],
   "ROOM NO.":[201,202,203,204,205,206,207,208,209,200,401,402,403,404]}
  
  


  f={"Services":["X-Ray","MRI","CT Scan","Endoscopy","Dialysis","Ultrasound ","EEG","ENMG","ECG"],
   "Room no.":[101,102,103,104,105,301,302,303,304]}
   
  



  while True:
    print("""
    
##====================================##  
||                                    ||
|| CHOOSE ONE OF THE GIVEN OPTION :-  ||
||____________________________________||
||                                    ||
|| 1. Register yourself               ||
|| 2. Appointment                     ||
|| 3. List of Doctors                 ||
|| 4. Services available              ||
|| 5. To modify data                  ||
|| 6. Back                            ||
||                                    ||
##====================================##
""")
    x=int(input("""YOUR OPTION:-"""))
    
    
    if x==1:
       print(" ")
       print(dat())
              
    
    elif x==2:
       print(" ")
       print(ret())
      
        
    elif x==3:
       print(" ")
       print("-----FOLLOWING DOCTORS ARE AVAILABLE-----")
       print(" ")
       print(df)
          
    
    elif x==4:
       print(" ")
       print("-----FOLLOWING SERVICES ARE AVAILABLE------")
       print(" ")
       print(dt)
       print(' ')
       print("To avail any of these please contact on our no.:- 9211420420")
    
        
    elif x==5:
       print(" ")
       
       
       while True:
           print("""
    __________________________      
    |                        |
    |SELECT WHAT TO CHANGE:- |
    |------------------------|
    |1.Name                  | 
    |2.Age                   |
    |3.Gender                |
    |4.Phone no.             |
    |5.Blood group           |
    |6.Back                  | 
    |________________________|
           """)
                      
           s=int(input("ENTER YOUR CHOICE:-"))

           if s==1:
               print(name())
               break

           elif s==2:
               print(age())
               break

           elif s==3:
               print(gen())
               break

           elif s==4:
               print(ph())
               break 
           
           elif s==5:
               print(bg())
               
           elif s==6:
               break
               
           else:
               print(" ")
               print("""~!~!~!~WRONG CHOICE PLEASE ENTER VALID VALUE~!~!~!~""")
               
          
    elif x==6:
        
           break
    
    
    else:
        print(" ")
        print("~!~!~!~WRONG CHOICE PLEASE ENTER A VALID VALUE~!~!~!~")
        
              

con.close()

