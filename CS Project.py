import mysql.connector as sqltor
from prettytable import PrettyTable
import random as rd
import datetime


con=sqltor.connect(host="localhost",user="root",password="solace1986")
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

cur.execute("create table if not exists pharmacy"
            "("
            "medid int(4) primary key,"
            "medname varchar(30),"
            "symptoms varchar(20),"
            "weight int(4),"
            "cost int(4))")

       

print("""
                  ____________________________________________________                   
        
                             WELCOME TO RED CROSS HOSPITAL

                  ____________________________________________________                
          """)

while True:
 print(""" 
      
    
        
        _______________                _______________                ____________
        |             |                |             |                |          |
        | 1. PATIENT  |                | 2. PHARMACY |                | 3. EXIT  |
        |_____________|                |_____________|                |__________|
        
         
        
        """)
 e=input("|| ENTER YOUR CHOICE ||:-")
 
 if e=="1" :
     
  def dat():
        while True:
            idn=input("Enter your Aadhaar no.(last three digits):")
            if len(idn)==3 :
                break
            else:
                print("~!~!~!~~3 digits required~~!~!~!~")
               
        name=input("Enter name of patient:")
        while True:
            age=int(input("Enter patient age:"))
            if type(age)!=int:
                print("~!~!~!~~digits required~~!~!~!~")
            else:
                break

        
        while True:
            gen=input("Gender M/F:")
            if gen==("M") or gen==("F"):
                break
            else:
                print("~!~!~!~~ M/F only ~~!~!~!~")
        
        while True:
            ph=input("Enter phone no.:")
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
            print("""     Aadhaar no.:-""",i[0])
            print('''     Name:-''',i[1])
            print('''     Age:-''',i[2])
            print('''     Gender:-''',i[3])
            print('''     Phone:-''',i[4])
            print('''     Bloodgroup:-''',i[5])
        return("")
       


  def name():
        adr=int(input('ENTER YOUR AADHAAR NO:'))
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
            print("""     Aadhaar no.:-""",i[0])
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
                print("""     Aadhaar no.:-""",row[0])
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
      |2.Dentist            |
      |3.Psychiatrist       |
      |4.Neurologist        |
      |5.Opthamologist      |
      |6.MI Room            |
      |7.Back               |
      |_____________________|
                 ''')
                
                 x=int(input("Enter choice:-"))
                
                 if x==1:
                    i=("Dr. Amit \nRoom no:- 201")
                    j=("Dr. Rahul \nRoom no:- 202")
                    q=(i,j)
                    h=rd.choice(q)
                    apdate=str(input("Enter date for appointment"))
                    print(" ")
                    print("Your appointment is fixed with",h,"\nDate:-",apdate)
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                 elif x==2:
                    i=("Dr. Aditi \nRoom no. 207")
                    j=("Dr. Arjun \nRoom no. 208")
                    q=(i,j)
                    h=rd.choice(q)
                    apdate=str(input("Enter date for appointment"))
                    print(" ")
                    print("Your appointment is fixed with",h,"\nDate:-",apdate)
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
               
                 elif x==3:
                    i=("Dr. Divya \nRoom no. 203")
                    j=("Dr. Gaurika \nRoom no. 204")
                    q=(i,j)
                    h=rd.choice(q)
                    apdate=str(input("Enter date for appointment"))
                    print(' ')
                    print("Your appointment is fixed with",h,"\nDate:-",apdate)
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                 elif x==4:
                    i=("Dr. Ajay, \nRoom no. 209")
                    j=("Dr. Garima \nRoom no. 200")
                    q=(i,j)
                    h=rd.choice(q)
                    apdate=str(input("Enter date for appointment"))
                    print(' ')
                    print("Your appointment is fixed with",h,"\nDate:-",apdate)
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                 elif x==5:
                    i=("Dr. Farhan \nRoom no. 205")
                    j=("Dr. Ishita \nRoom no. 206")
                    q=(i,j)
                    h=rd.choice(q)
                    apdate=str(input("Enter date for appointment"))
                    print(' ')
                    print("Your appointment is fixed with",h,"\nDate:-",apdate)
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-:",o)
                    break
                 elif x==6:
                    i=("Dr. Armaan \nRoom no. 001")
                    j=("Dr. Kartik \nRoom no. 002")
                    k=("Dr. Nayra \nRoom no. 003")
                    l=("Dr. Samaira \nRoom no. 004")
                    q=(i,j,k,l)
                    h=rd.choice(q)
                    apdate=str(input("Enter date for appointment"))
                    print(" ")
                    print("Your appointment is fixed with",h,"\nDate:-",apdate)
                    u=(12,43,54,71,32,65)
                    o=rd.choice(u)
                    print("Appointment no:-",o)
                    break
                
                 elif x==7:
                    break
                 else:
                  print("~!~!~!~WRONG OPTION PLEASE ENTER VALID VALUE~!~!~!~")
                  
     
        return(" ")
            
                
    
  l={"NAME OF DOCTOR":["Dr. Amit","Dr. Rahul","Dr. Aditi","Dr. Arjun","Dr. Divya","Dr. Gaurika","Dr. Ajay","Dr. Garima","Dr. Farhan",
                     "Dr. Ishita",'Dr. Armaan','Dr. Kartik','Dr. Nayra','Dr. Samaira'],
   "DEPARTMENT":["Cardiologist","Cardiologist","Dentist","Dentist","Psychiatrist","Psychiatrist","Neurologist","Neurologist","Opthamologist",
                 "Opthamologist",'MI room','MI room','MI room','MI room'],
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
       print("-----FOLLOWING DOCTORS ARE AVAILABLE:-----")
       print(" ")
       doc=["Dr. Amit - Cardiologist","Dr. Rahul - Cardiologist","Dr. Aditi - Dentist","Dr. Arjun - Dentist","Dr. Divya - Psychiatrist","Dr. Gaurika - Psychiatrist","Dr. Ajay - Neurologist","Dr. Garima - Neurologist","Dr. Farhan - Opthamologist",
                     "Dr. Ishita - Opthamologist",'Dr. Armaan - MI Room','Dr. Kartik - MI Room','Dr. Nayra - MI Room','Dr. Samaira - MI Room']
  
  
       for i in doc:
           print(i)
          
    
    elif x==4:
       print(" ")
       print("-----FOLLOWING SERVICES ARE AVAILABLE:------")
       print(" ")
       services=["X-Ray","MRI","CT Scan","Endoscopy","Dialysis","Ultrasound ","EEG","ENMG","ECG"]
       for i in services:
           print(i)
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

 elif e=="2":
     print("""
                  ____________________________________________________                   
        
                             WELCOME TO RED CROSS PHARMACY

                  ____________________________________________________                
          """)
     while True:
         med=[]
         quantity=[]
         amount=[]
         disp=[]
         tot=0
         tot2=0
         

         def extract():
             name=input("Enter medicine name:")
             select="select medname, cost from pharmacy where medname=%s"
             val=(name,)
             cur.execute(select,val)
             for x in cur:
                 med.append(x)
             for i in range (len(med)):
                 med[i]=list(med[i])
             print (med)
             qty=int(input("Enter quantity of medicine (in terms of packets):"))
             quantity.append(qty)
             print(quantity)

         def bill():
             for i in range(0,len(med)):
                 amount.append(med[i][1]*quantity[i])
             print(amount)

         def invoice():
             for i in range(len(med)):
                 med[i].append(quantity[i])
                 med[i].append(amount[i])
             print(med)
             
             print('''
            -----------------------  
            | RED CROSS PHARMACY  |
            |        BILL         |
            -----------------------
                   ''')
             t1 = PrettyTable(['Product Name', 'Cost', 'Qty', 'Total'])
             for i in range(len(med)):
                 t1.add_row(med[i])
             print(t1)
             

         def total():
             tot=0
             tot2=0
             for x in amount:
                 tot=tot+x
             tot2=tot+tot*0.18
             print(' ')
             print('Your bill amount is:',tot)
             print('GST 18%')
             print('Your total bill amount is:',tot2)

         def display():
             print('''
             -----------------------  
             | MEDICINES AVAILABLE |
             -----------------------    
                ''')
             cur.execute("select * from pharmacy")
             for x in cur:
                 disp.append(x)
             t2 = PrettyTable(['MedID', 'MedName', 'Symptoms', 'Weight', 'Cost'])
             for i in range(len(disp)):
                 t2.add_row(disp[i])
             print(t2)




        

         print('')

         display()
         extract()
         while True:
             ch=input("Would you like to add more? (y/n):")
             if ch=='y':
                 extract()
            
             else:
                 break
         bill()
         invoice()
         total()
         break
         
             
        
    
     
            
         
                        
 elif e=="3":
        print(" ")
        print("\n"
              "      \n"
              "   ##======================================================##\n"
              "   || _____        ___                          ___        ||\n"
              "   ||   |   |   | |   | |\   | |  /      |   | |   | |   | ||\n"
              "   ||   |   |___| |___| | \  | |_/       |___| |   | |   | ||\n"
              "   ||   |   |   | |   | |  \ | | \           | |   | |   | ||\n"
              "   ||   |   |   | |   | |   \| |  \       ___| |___| |___| ||\n"
              "   ##======================================================##\n"
              "\n")
              
        break
 
    
 else:
        print(" ")
        print("~~~~PLEASE ENTER 1,2 OR 3~~~~")

        
              

con.close()

