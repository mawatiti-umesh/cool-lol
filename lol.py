
# PYTHON SOURCE CODE:

# ---------------------------------------|
# ✨ Pydroid Hills Housing Society
# ---------------------------------------|

import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='school',database='housingsociety')
cursor=con.cursor()

###################### Following are the variable used for while loop generation ###################### 
soc=1
soc1=0
soc2=0
soc3=0
soc4=0
soc5=0
soc6=0
soc7=0
soc8=0
soc9=0

def house():
    print('''
                        ███
                      ███████
                   ██████████████
                ████████████████████
             ████  PYDROID HILLS  █████
          ███████ HOUSING SOCIETY ████████
         ██████████████████████████████████
          █░░░░██░░░░██████████░░░░██░░░░█
          █░░░░██░░░░██████████░░░░██░░░░█
          ████████████████████████████████
          █░░░░██░░░░██████████░░░░██░░░░█
          █░░░░██░░░░██████████░░░░██░░░░█
          ████████████████████████████████
          ████████████████████████████████
          █░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
          █░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
          ████████████▒▒▒░░▒▒▒████████████
          █░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
          █░░░░██░░░░█▒▒▒▒▒▒▒▒█░░░░██░░░░█
          ████████████▒▒▒▒▒▒▒▒████████████
         ████████████▓▓▓▓▓▓▓▓▓▓████████████
         ███████████▓▓▓▓▓▓▓▓▓▓▓▓███████████''')
    
house()


while soc==1: #While loop started

    print("                                                    ")
    print("✨ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ✨")
    print("                                                    ")
    print("  <<<< 𝐒𝐔𝐁𝐌𝐈𝐓𝐓𝐄𝐃 𝐁𝐘 𝐓𝐇𝐄 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 𝐒𝐓𝐔𝐃𝐄𝐍𝐓𝐒  >>>>")      
    print("                                                    ")
    print("                  𝓐𝓖𝓐𝓜 𝓢𝓘𝓝𝓖𝓗 (𝓟𝓒𝓜)               ")
    print("                𝓔𝓚𝓐𝓖𝓡𝓐  𝓖𝓤𝓟𝓣𝓐 (𝓟𝓒𝓜)              ")
    print("          𝓚𝓤𝓝𝓐𝓛 𝓢𝓡𝓘𝓥𝓐𝓢𝓣𝓐𝓥𝓐 (𝓒𝓞𝓜𝓜𝓔𝓡𝓒𝓔)         ")
    print("                                                        ")
    print("✨ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ✨") 
    print("                                                    ")
    
    print('-------------------------------------') 
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟏 𝐓𝐎 𝐄𝐍𝐓𝐄𝐑 𝐎𝐖𝐍𝐄𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒      ")
    #To Enter New Owner Details into Table ownerdet.
    print('-------------------------------------')                                                        
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟐 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐃𝐄𝐓𝐀𝐈𝐋𝐒          ")
    #To Display Details From Tables ownerdet & olddet.
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟑 𝐓𝐎 𝐄𝐍𝐓𝐄𝐑 𝐒𝐎𝐂𝐈𝐄𝐓𝐘 𝐓𝐀𝐗𝐄𝐒        ")
    #To Enter Society Details into Table societymain.
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟒 𝐓𝐎 𝐄𝐍𝐓𝐄𝐑 𝐇𝐎𝐔𝐒𝐈𝐍𝐆 𝐓𝐀𝐗𝐄𝐒        ")
    #To Enter Housing Details into Table housing_tax.
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟓 𝐓𝐎 𝐄𝐍𝐓𝐄𝐑  𝐄𝐍𝐓𝐑𝐘 𝐃𝐄𝐓𝐀𝐈𝐋𝐒      ")
    #To Enter Entry Details into Table residentdet & visitordet respectively.
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟔 𝐓𝐎 𝐄𝐍𝐓𝐄𝐑 𝐏𝐀𝐑𝐊𝐈𝐍𝐆 𝐃𝐄𝐓𝐀𝐈𝐋𝐒       ")
    #To Enter Parking Details into Table parkingdet.
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟕 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐏𝐀𝐑𝐊𝐈𝐍𝐆 𝐃𝐄𝐓𝐀𝐈𝐋𝐒     ")
    #To Display Parking Details From Table parkingdet.
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟖 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐄𝐍𝐓𝐑𝐘 𝐃𝐄𝐓𝐀𝐈𝐋𝐒       ")
    #To Display Entry Details from Table residentdet & visitordet respectively.
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟗 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐁𝐈𝐋𝐋𝐒            ")
    #To Display Bill Details from Table housing_tax & societymain respectively
    print('-------------------------------------')
    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟏𝐎 𝐓𝐎 𝐄𝐗𝐈𝐓                 ")
    #To EXIT the whole program
    print('-------------------------------------')
    print("                                                    ")

    CHOICE=int(input("ENTER ANY CHOICE: "))    

    def welcome_message(): #Welcome Message 
        
                print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
                print('   𝓦𝓔𝓛𝓒𝓞𝓜𝓔 𝓣𝓞 𝓟𝓨𝓓𝓡𝓞𝓘𝓓 𝓗𝓘𝓛𝓛𝓢 𝓗𝓞𝓤𝓢𝓘𝓝𝓖 𝓢𝓞𝓒𝓘𝓔𝓣𝓨')    
                #Greeting Message & Name of the Society
                print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
                print("                                                    ")
                

    def owndet(): # Inserting values into Table ownerdet

        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print('𝐅𝐈𝐋𝐋 𝐓𝐇𝐄𝐒𝐄 𝐃𝐄𝐓𝐀𝐈𝐋𝐒 𝐓𝐎 𝐂𝐑𝐄𝐀𝐓𝐄 𝐀𝐂𝐂𝐎𝐔𝐍𝐓')         
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print("                                                    ")
        
       
        
        Owner_Id=input('Enter Owner ID (stars from 101) : ')
        Owner_Name=input("Enter Owner's Name: ")
        DOB=input('Enter Date Of Birth (YYYY-MM-DD): ')                        
        # Date to be entered in (YYYY-MM-DD) Format
        Acquired_On=input('Enter Date of Purchase (YYYY-MM-DD): ')             
        # Date to be entered in (YYYY-MM-DD) Format
        Second_Add=input('Enter Second Add. : ')
        Family_Count=int(input('Enter No. of Family Members : '))
        Sex=input('Enter Gender (M/F) : ')                                     
        # Enter (M) for Male & (F) for Female
        Mobile_No=int(input('Enter 10 digit Mobile No. : '))                   
        # Enter Mobile Number in 10 digit fromat
        Occupation=input('Enter Occupation : ')
        S=str(Owner_Id)
        R=input('Enter House Type 3-BHK/5-BHK : ')                             
        # Enter 3-BHK/5-BHK 
        T=R+" "+"("+S+")"
        House_Id=T
        Email_Id=input('Enter E-Mail-ID: ')                                    
        # Enter Email-Id
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        
        value=(Owner_Id,Owner_Name,DOB,Acquired_On,Second_Add,\
               Family_Count,Sex,Mobile_No,Occupation,House_Id,Email_Id)
        query='insert into ownerdet values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        
        cursor.execute(query,value)
        con.commit()
        
        print("𝐎𝐰𝐧𝐞𝐫-𝐈𝐃 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Owner_Id)
        #THANK YOU MESSAGE
        print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>") 
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')

    def societymain():    #Inserting values into Table societymain
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print('<<<<   𝗙𝗜𝗟𝗟 𝗦𝗢𝗖𝗜𝗘𝗧𝗬 𝗠𝗢𝗡𝗧𝗛𝗟𝗬 𝗗𝗘𝗧𝗔𝗜𝗟𝗦   >>>>')
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print("                                                    ")
        
        Sno=input('Enter Serial No. : ')                                                                             
        Months=input("Enter Month Name: ")
        Water_Tax=int(input('Enter Water Tax: '))
        Electricity_Bill=int(input('Enter Electricity :'))
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        
        value =(Sno,Months,Water_Tax,Electricity_Bill)
        query='insert into societymain value(%s,%s,%s,%s)'
        
        cursor.execute(query,value)
        con.commit()
        
        print("𝐒𝐞𝐫𝐢𝐚𝐥 𝐍𝐮𝐦𝐛𝐞𝐫 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Sno)
        #THANK YOU MESSAGE
        print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>")
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')

    def residentdet():     # Inserting values into Table residentdet
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=')
        print('<<<<  𝗙𝗜𝗟𝗟 𝗧𝗢 𝗘𝗡𝗧𝗘𝗥 𝗥𝗘𝗦𝗜𝗗𝗘𝗡𝗧 𝗗𝗘𝗧𝗔𝗜𝗟𝗦  >>>>')
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=')
        print("                                                    ")                                              
        
        
              
        Owner_Id=input('Enter Owner ID (stars from 101) : ')                   
        # Primary Key (Owner_Id)
        Arrival_Time=input("Enter Arrival time  (YYYY-MM-DD HH:MM:SS) : ")     
        # Time to be entered in (YYYY-MM-DD HH:MM:SS) Format
        Departure_Time=input('Enter Departure time (YYYY-MM-DD HH:MM:SS) : ')  
        # Time to be entered in (YYYY-MM-DD HH:MM:SS) Format
        TempInCelsius=eval(input('Enter Current Temperature (Celsius) : '))    
        # Enter Temperature in Celsius
        print('====================================')
        value=(Owner_Id,Arrival_Time,Departure_Time,TempInCelsius)
        query='insert into residentdet values(%s,%s,%s,%s)'
        
        cursor.execute(query,value)
        con.commit()
        
        print("𝐎𝐰𝐧𝐞𝐫-𝐈𝐃 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Owner_Id)
        #THANK YOU MESSAGE
        print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>") 
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=')

    def visitordet():   # Inserting values into Table visitordet
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=')
        print('<<<<  𝗙𝗜𝗟𝗟 𝗧𝗢 𝗘𝗡𝗧𝗘𝗥 𝐕𝐈𝐒𝐈𝐓𝐎𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒  >>>>')
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=')
        print("                                                    ")
        
        Sno=input('Enter Serial No. : ')
        Name=input("Enter Name of the Visitor: ")
        Arrival_Time=input("Enter Arrival time  (YYYY-MM-DD HH:MM:SS) : ")     
        # Time to be entered in (YYYY-MM-DD HH:MM:SS) Format
        Departure_Time=input('Enter Departure time (YYYY-MM-DD HH:MM:SS) : ')  
        # Time to be entered in (YYYY-MM-DD HH:MM:SS) Format
        TempInCelsius=eval(input('Enter current temperature : '))              
        # Enter Temperature in Celsius
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=')
        
        value =(Sno,Name,Arrival_Time,Departure_Time,TempInCelsius)
        query='insert into visitordet value(%s,%s,%s,%s,%s)'
        
        cursor.execute(query,value)
        con.commit()
        
        print("𝐒𝐞𝐫𝐢𝐚𝐥 𝐍𝐮𝐦𝐛𝐞𝐫 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Sno)
        print("                                                    ")
        #THANK YOU MESSAGE
        print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>")
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=')
        

    def bike(): # Function used for parking of Owner having Bike
                   
           Owner_Id=input('Enter your Owner ID (stars from 101) : ')            
           NO1 = int(input("ENTER NO. OF VEHICLES: "))
           Vehicle="Bike"+"-"+str(NO1)
           Monthly_Bill = 500*NO1
           Yearly_Bill = Monthly_Bill*12
 
           print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
           value=(Owner_Id,Vehicle,Monthly_Bill,Yearly_Bill)
           query='insert into parkingdet values(%s,%s,%s,%s)'
            
           cursor.execute(query,value)
           con.commit()
            
           print("𝐎𝐰𝐧𝐞𝐫-𝐈𝐃 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Owner_Id)
           #THANK YOU MESSAGE
           print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>") 
           print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==') 
           
           
    def car():  # Function used for parking of Owner having Car 
        
        Owner_Id=input('Enter your Owner ID (stars from 101) : ') 
        NO = int(input("ENTER NO. OF VEHICLES: "))
        Vehicle="Car"+"-"+str(NO)
        Monthly_Bill = 1000*NO
        Yearly_Bill = Monthly_Bill*12
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        value=(Owner_Id,Vehicle,Monthly_Bill,Yearly_Bill)
        query='insert into parkingdet values(%s,%s,%s,%s)'
         
        cursor.execute(query,value)
        con.commit()
         
        print("𝐎𝐰𝐧𝐞𝐫-𝐈𝐃 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Owner_Id)
        #THANK YOU MESSAGE
        print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>") 
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==') 
        
    def Both():  # Function used for parking of Owner having both Car & Bike
            
         Owner_Id=input('Enter your Owner ID (stars from 101) : ')
         Vehicle="Car,Bike"
         Monthly_Bill = 1500
         Yearly_Bill = 1500*12
         
         print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
         value=(Owner_Id,Vehicle,Monthly_Bill,Yearly_Bill)
         query='insert into parkingdet values(%s,%s,%s,%s)'
          
         cursor.execute(query,value)
         con.commit()
          
         print("𝐎𝐰𝐧𝐞𝐫-𝐈𝐃 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Owner_Id)
         #THANK YOU MESSAGE
         print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>") 
         print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')    


    def HouseTaxes():  # To Enter details into Table housing_tax
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print('<<<<  𝐅𝐈𝐋𝐋 𝐇𝐎𝐔𝐒𝐈𝐍𝐆 𝐓𝐀𝐗 𝐃𝐄𝐓𝐀𝐈𝐋𝐒   >>>>')
        print("                                                    ")
        
        Owner_Id=int(input('Enter Owner ID (stars from 101) : '))
        #Primary Key (Owner_Id)              
        C=str(Owner_Id)
        A=input('Enter House Type 3-BHK/5-BHK : ')
        B=A+" "+"("+C+")"
        House_Id=B
        
        if A == "3-BHK":
            Maintenance=5100                                                   
            # Maintenance for 3-BHK is updated.
            
        else:
            Maintenance=6800                                                   
            # Maintenance for 5-BHK is updated.
        
        Electricity_Bill=int(input('Enter Electricity Bill : '))               
        # Enter Electricity Bill here.
        print("                                                    ")
        
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        
        value =(Owner_Id,House_Id,Maintenance,Electricity_Bill)
        query='insert into housing_tax value(%s,%s,%s,%s)'
        
        cursor.execute(query,value)
        con.commit()
        
        print("𝐎𝐰𝐧𝐞𝐫-𝐈𝐃 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐄𝐧𝐭𝐞𝐫𝐞𝐝 𝐢𝐬",Owner_Id)
        #THANK YOU MESSAGE
        print(" <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>") 
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        

    def exit():     # Exit function
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print("            <<<<         𝓣𝓱𝓪𝓷𝓴 𝓨𝓸𝓾          >>>>")
        print("Address- Sector-19 Pydroid Housing Society, Golf City, Lucknow")
        print("                      Pincode: 226000")
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print("                  ----:Contact Number:----")
        print("                  Landline: 0522-2244-304")
        print("                   Reception: 9090909087")
        print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
        print("                                                    ")
        print("✨ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ✨")
        print("                                                    ")
        print("        <<<< 𝐒𝐔𝐁𝐌𝐈𝐓𝐓𝐄𝐃 𝐁𝐘 𝐓𝐇𝐄 𝐅𝐎𝐋𝐋𝐎𝐖𝐈𝐍𝐆 𝐒𝐓𝐔𝐃𝐄𝐍𝐓𝐒  >>>>")      
        print("                                                    ")
        print("                    𝓐𝓖𝓐𝓜 𝓢𝓘𝓝𝓖𝓗 (𝓟𝓒𝓜)               ")
        print("                  𝓔𝓚𝓐𝓖𝓡𝓐  𝓖𝓤𝓟𝓣𝓐 (𝓟𝓒𝓜)              ")
        print("            𝓚𝓤𝓝𝓐𝓛 𝓢𝓡𝓘𝓥𝓐𝓢𝓣𝓐𝓥𝓐 (𝓒𝓞𝓜𝓜𝓔𝓡𝓒𝓔)         ")
        print("                                                        ")
        print("          𝐔𝐧𝐝𝐞𝐫 𝐭𝐡𝐞 𝐆𝐮𝐢𝐝𝐚𝐧𝐜𝐞 𝐨𝐟 𝐏𝐫𝐚𝐜𝐡𝐢 𝐏𝐚𝐭𝐡𝐚𝐤 𝐌𝐚❜𝐚𝐦               ")
        print("✨ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ ✨")
        print("                                                    ")    
            
    
    if CHOICE == 1: 
        soc3=1 #Used for while loop
        while soc3 == 1: #While loop started
            welcome_message()  #Function Call
            print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
            print("<<<<        𝐂𝐇𝐎𝐎𝐒𝐄 𝟏 𝐓𝐎 𝗘𝗡𝗧𝗘𝗥 𝐀 𝐍𝐄𝐖 𝐑𝐄𝐂𝐎𝐑𝐃     >>>>")       
            # Enter new record into Table ownerdet
            print("<<<<   𝐂𝐇𝐎𝐎𝐒𝐄 𝟐 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐀  𝐏𝐑𝐄𝐕𝐈𝐎𝐔𝐒 𝐑𝐄𝐂𝐎𝐑𝐃  >>>>")        
            # Updation of previous Record
            print("<<<<               𝐂𝐇𝐎𝐎𝐒𝐄 𝟑 𝐓𝐎 𝐄𝐗𝐈𝐓               >>>>")       
            # Press 3 to Exit from this loop.
            print("                                                    ")
            
            B=int(input("ENTER CHOICE: "))
            print("                                                    ")
            
            if B == 1:
                owndet() #Function Call
                
            elif B == 2:                                                       
                # To update the following details choose the appropriate Option
                soc4=1 #Used for while loop
                while soc4 == 1: # While loop started
                    print('-------------------------------------') 
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟏 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐎𝐖𝐍𝐄𝐑 𝐍𝐀𝐌𝐄     ")    
                    # 1 To update Owner name
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟐 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐃𝐀𝐓𝐄 𝐎𝐅 𝐁𝐈𝐑𝐓𝐇   ")   
                    # 2 To update Date of Birth
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟑 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐒𝐄𝐂𝐎𝐍𝐃 𝐀𝐃𝐃𝐑𝐄𝐒𝐒  ")   
                    # 3 To update Second address
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟒 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐅𝐀𝐌𝐈𝐋𝐘 𝐂𝐎𝐔𝐍𝐓   ")    
                    # 4 To update Family count
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟓 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐒𝐄𝐗       ")           
                    # 5 To update Gender
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟔 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐌𝐎𝐁𝐈𝐋𝐄 𝐍𝐔𝐌𝐁𝐄𝐑  ")   
                    # 6 To update Mobile Number
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟕 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐎𝐂𝐂𝐔𝐏𝐀𝐓𝐈𝐎𝐍    ")     
                    # 7 To update Occupation
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟖 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐇𝐎𝐔𝐒𝐄-𝐈𝐃     ")       
                    # 8 To update House-Id
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟗 𝐓𝐎 𝐔𝐏𝐃𝐀𝐓𝐄 𝐄𝐌𝐀𝐈𝐋-𝐈𝐃     ")       
                    # 9 To update Email-Id
                    print('-------------------------------------') 
                    
                    print("✨ 𝐏𝐑𝐄𝐒𝐒 𝟏𝟎 𝐓𝐎 𝐄𝐗𝐈𝐓           ")            
                    # 10 To Exit from this loop
                    print('-------------------------------------') 
                    print("                                                    ")
                    
                    CHOIce=int(input("ENTER CHOICE: "))
                    
                    
                    if CHOIce == 1:  # 1 To update Owner name
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        Owner_Name=input("ENTER New Owner Name : ")
                        sql_update_query = """Update Ownerdet set Owner_Name \
                            = %s where Owner_Id = %s"""
                        input_data = (Owner_Name, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                        
                        
                    elif CHOIce == 2:   # 2 To update Date of Birth
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        DOB=input("ENTER DATE OF BIRTH : ")
                        sql_update_query = """Update Ownerdet set DOB = %s where\
                            Owner_Id = %s"""
                        input_data = (DOB, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                        
                    
                    elif CHOIce == 3:   # 3 To update Second address
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        Second_Add=input("ENTER SECOND ADDRESS : ")
                        sql_update_query = """Update Ownerdet set Second_Add = \
                            %s where Owner_Id = %s"""
                        input_data = (Second_Add, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                        
                    
                    elif CHOIce == 4:   # 4 To update Family count
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        Family_Count=input("ENTER FAMILY COUNT : ")
                        sql_update_query = """Update Ownerdet set Family_Count =\
                            %s where Owner_Id = %s"""
                        input_data = (Family_Count, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                        
                    
                    elif CHOIce == 5:   # 5 To update Gender
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        Sex=input("ENTER Gender : ")
                        sql_update_query = """Update Ownerdet set Sex = %s \
                            where Owner_Id = %s"""
                        input_data = (Sex, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                        
                    
                    elif CHOIce == 6:    # 6 To update Mobile Number
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        Mobile_No=input("ENTER New Mobile No. : ")
                        sql_update_query = """Update Ownerdet set Mobile_No = %s \
                            where Owner_Id = %s"""
                        input_data = (Mobile_No, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                        
                        
                    elif CHOIce == 7:    # 7 To update Occupation
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        Occupation=input("ENTER Occupation : ")
                        sql_update_query = """Update Ownerdet set Occupation = %s \
                            where Owner_Id = %s"""
                        input_data = (Occupation, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()  
                        
                    
                    elif CHOIce == 8:    # 8 To update House-Id
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        House_Id=input("ENTER House_Id : ")
                        sql_update_query = """Update Ownerdet set House_Id = %s \
                            where Owner_Id = %s"""
                        input_data = (House_Id, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                     
                        
                    elif CHOIce == 9:    # 9 To update Email-Id
                        cursor=con.cursor()
                        Owner_Id=input("ENTER Owner Id where value to be changed: ")
                        Email_Id=input("ENTER Email_Id : ")
                        sql_update_query = """Update Ownerdet set Email_Id = %s\
                            where Owner_Id = %s"""
                        input_data = (Email_Id, Owner_Id)
                        cursor.execute(sql_update_query, input_data)
                        con.commit()
                        
                    elif CHOIce == 10:    # 10 To Exit from this loop
                        soc4=0   #While loop terminated
                        
                    else:
                        print("++++++++++++++++++++++++++")
                        print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
                        print("++++++++++++++++++++++++++")
                     
            elif B == 3:
                soc3=0   #While loop terminated
                
            else:
                print("++++++++++++++++++++++++++")
                print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
                print("++++++++++++++++++++++++++")


    elif CHOICE == 2:
        
        soc6=1    #Used for while loop
        while soc6 == 1:    # While loop started
            print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟏 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐎𝐖𝐍𝐄𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒  ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟐 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐎𝐋𝐃 𝐃𝐄𝐓𝐀𝐈𝐋𝐒    ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟑 𝐓𝐎 𝐄𝐗𝐈𝐓              ")
            print("                                                    ")
            
            CHOICE2=int(input("ENTER CHOICE: "))
            
            if CHOICE2 == 1:
                
                welcome_message()  #Function Call
                        
                cursor.execute("select * from ownerdet")
                data = cursor.fetchall()  #Fetch data command
                count = cursor.rowcount

                print("𝐓𝐨𝐭𝐚𝐥 𝐍𝐨. 𝐨𝐟 𝐑𝐨𝐰𝐬 𝐑𝐞𝐭𝐫𝐢𝐞𝐯𝐞𝐝 : ",count)
                print("|Owner_Id|Owner_Name|DOB|Acquired_On|Second_Add| \
                      Family_Count|Sex|Mobile_No|Occupation|House_Id|Email_Id|")

                for row in data:
                    print('+++++++++++++++++++++++++++++++++++')
                    print('-----------------------------------')
                    print("Owner ID: ",row[0])
                    print('-----------------------------------')
                    print("Owner Name: ",row[1])
                    print('-----------------------------------')
                    print("DOB : ",row[2])
                    print('-----------------------------------')
                    print("Acquired_On: ",row[3])
                    print('-----------------------------------')
                    print("Second_Add: ",row[4])
                    print('-----------------------------------')
                    print("Family_Count: ",row[5])
                    print('-----------------------------------')
                    print("Sex: ",row[6])
                    print('-----------------------------------')
                    print("Mobile_No.: ",row[7])
                    print('-----------------------------------')
                    print("Occupation: ",row[8])
                    print('-----------------------------------')
                    print("House-ID: ",row[9])
                    print('-----------------------------------')
                    print("Email-ID : ",row[10])
                    print('-----------------------------------')
                      
                    
            elif CHOICE2 == 2:
                
                welcome_message()  #Function Call
                
                cursor.execute("select * from olddet")
                data = cursor.fetchall()  #Fetch data command
                count = cursor.rowcount
                
                print('-----------------------------------')
                print("𝐓𝐨𝐭𝐚𝐥 𝐍𝐨. 𝐨𝐟 𝐑𝐨𝐰𝐬 𝐑𝐞𝐭𝐫𝐢𝐞𝐯𝐞𝐝 : ",count)
                print('-----------------------------------')
                

                for row in data:
                    print('+++++++++++++++++++++++++++++++++++')
                    print('-----------------------------------')
                    print("Owner ID: ",row[0])
                    print('-----------------------------------')
                    print("Name: : ",row[1])
                    print('-----------------------------------')
                    print("DOB : ",row[2])
                    print('-----------------------------------')
                    print("Acquired_On: ",row[3])
                    print('-----------------------------------')
                    print("Second_Add: ",row[4])
                    print('-----------------------------------')
                    print("Family_Count: ",row[5])
                    print('-----------------------------------')
                    print("Sex: ",row[6])
                    print('-----------------------------------')
                    print("Mobile_No: ",row[7])
                    print('-----------------------------------')
                    print("Occupation: ",row[8])
                    print('-----------------------------------')
                    print("House Type: ",row[9])
                    print('-----------------------------------')
                    print("Email-ID : ",row[3])
                    print('-----------------------------------')
                
            elif CHOICE2 == 3:
                soc6 = 0       #While loop terminated 
                
            else:
                print("++++++++++++++++++++++++++")
                print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
                print("++++++++++++++++++++++++++")
        
            
            
    elif CHOICE == 3:
         welcome_message()  #Function Call
         societymain()  #Function Call
         
    elif CHOICE == 4:
        welcome_message()  #Function Call
        HouseTaxes()  #Function Call
        
    elif CHOICE == 5:
        soc2=1 #Used for while loop
        while soc2 == 1: #While loop started
            welcome_message()
            
            print("                                                    ")
            print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟏 𝐓𝐎 𝐄𝐍𝐓𝐄𝐑 𝐑𝐄𝐒𝐈𝐃𝐄𝐍𝐓 𝐃𝐄𝐓𝐀𝐈𝐋𝐒  ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟐 𝐓𝐎 𝐄𝐍𝐓𝐄𝐑 𝐕𝐈𝐒𝐈𝐓𝐎𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒    ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟑 𝐓𝐎 𝐄𝐗𝐈𝐓                       ")
            print("                                                    ")
            
            Choice_1= int(input("ENTER CHOICE: "))
            
            if Choice_1 == 1:
                welcome_message()  #Function Call
                residentdet()  #Function Call
                
            elif Choice_1 == 2:
                welcome_message()  #Function Call
                visitordet()  #Function Call
                
            elif Choice_1 == 3:
                soc2 = 0    #While loop terminated
                
            else:
                print("++++++++++++++++++++++++++")
                print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
                print("++++++++++++++++++++++++++")
        


    elif CHOICE == 6:
        soc7=1 #Used for while loop
        while soc7 == 1: #While loop started
            welcome_message()
            
            print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
           
                     
            print("                                                    ")
            print("<<<< 𝐄𝐍𝐓𝐄𝐑 𝟏 𝐅𝐎𝐑 𝐁𝐈𝐊𝐄  >>>>")
            print("<<<< 𝐄𝐍𝐓𝐄𝐑 𝟐 𝐅𝐎𝐑 𝐂𝐀𝐑   >>>>")
            print("<<<< 𝐄𝐍𝐓𝐄𝐑 𝟑 𝐅𝐎𝐑 𝐁𝐎𝐓𝐇 >>>>")
            print("<<<< 𝐄𝐍𝐓𝐄𝐑 𝟒 𝐓𝐎 𝐄𝐗𝐈𝐓   >>>>")
            ChoiCe_1= int(input("ENTER CHOICE: "))
            
            if ChoiCe_1 == 1:
                welcome_message()  #Function Call
                bike()  #Function Call
                
            elif ChoiCe_1 == 2:
                welcome_message()  #Function Call
                car()  #Function Call
                
            elif ChoiCe_1 == 3:
                welcome_message()  #Function Call
                Both()  #Function Call    
                
            elif ChoiCe_1 == 4:
                soc7 = 0    #While loop terminated
                
            else:
                print("++++++++++++++++++++++++++")
                print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
                print("++++++++++++++++++++++++++")  


    elif CHOICE == 7:
        
        welcome_message()  #Function Call
        
        cursor.execute("select * from parkingdet")
        data = cursor.fetchall()
        count = cursor.rowcount

        print("𝐓𝐨𝐭𝐚𝐥 𝐍𝐨. 𝐨𝐟 𝐑𝐨𝐰𝐬 𝐑𝐞𝐭𝐫𝐢𝐞𝐯𝐞𝐝 : ",count)
        print("|Owner_Id | Vehicle | Monthly_Bill | Yearly_Bill |")

        for row in data:
            print('+++++++++++++++++++++++++++++++++++')
            print('-----------------------------------')
            print("Owner ID: ",row[0])
            print('-----------------------------------')
            print("Vehicle Type: ",row[1])
            print('-----------------------------------')
            print("Monthly Bill : ",row[2])
            print('-----------------------------------')
            print("Yearly_Bill: ",row[3])
            print('+++++++++++++++++++++++++++++++++++') 
            
    elif CHOICE == 8:
        soc5=1 #Used for while loop
        while soc5 == 1: #While loop started
            welcome_message()  #Function Call
            print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟏 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐑𝐄𝐒𝐈𝐃𝐄𝐍𝐓 𝐃𝐄𝐓𝐀𝐈𝐋𝐒  ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟐 𝐓𝐎 𝐃𝐈𝐒𝐏𝐋𝐀𝐘 𝐕𝐈𝐒𝐈𝐓𝐎𝐑 𝐃𝐄𝐓𝐀𝐈𝐋𝐒   ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟑 𝐓𝐎 𝐄𝐗𝐈𝐓                      ")
            print("                                                    ")

            
            CHOICE1=int(input("Enter Choice: "))
            
            if CHOICE1 == 1:
                cursor.execute("select * from residentdet")
                data = cursor.fetchall()  #Fetch data command
                count = cursor.rowcount
                print("𝐓𝐨𝐭𝐚𝐥 𝐍𝐨. 𝐨𝐟 𝐑𝐨𝐰𝐬 𝐑𝐞𝐭𝐫𝐢𝐞𝐯𝐞𝐝 : ",count)

                for row in data:
                    print('+++++++++++++++++++++++++++++++++++')
                    print('-----------------------------------')
                    print("Owner ID: ",row[0])
                    print('-----------------------------------')
                    print("Arrival Time: : ",row[1])
                    print('-----------------------------------')
                    print("Departure Time : ",row[2])
                    print('-----------------------------------')
                    print("Temperature in celsius : ",row[3])
                    print('-----------------------------------')
                     
            elif CHOICE1 == 2:
                cursor.execute("select * from visitordet")
                data = cursor.fetchall()  #Fetch data command
                count = cursor.rowcount
                print("𝐓𝐨𝐭𝐚𝐥 𝐍𝐨. 𝐨𝐟 𝐑𝐨𝐰𝐬 𝐑𝐞𝐭𝐫𝐢𝐞𝐯𝐞𝐝 : ",count)

                for row in data:
                    print('+++++++++++++++++++++++++++++++++++')
                    print('-----------------------------------')
                    print("Serial No. : ",row[0])
                    print('-----------------------------------')
                    print("Name: : ",row[1])
                    print('-----------------------------------')
                    print("Arrival Time: : ",row[2])
                    print('-----------------------------------')
                    print("Departure Time : ",row[3])
                    print('-----------------------------------')
                    print("Temperature in celsius : ",row[4])
                    print('-----------------------------------')
                   
            elif CHOICE1 == 3:
                soc5 = 0    #While loop terminated
                 
            else:
                print("++++++++++++++++++++++++++")
                print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
                print("++++++++++++++++++++++++++")
      
    elif CHOICE == 9:
        
        soc1=1  #Used for while loop
        while soc1 == 1: #While loop started
            welcome_message()  #Function Call
            print('=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷=̷==')
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟏 𝐓𝐎 𝐏𝐑𝐈𝐍𝐓 𝐇𝐎𝐔𝐒𝐈𝐍𝐆 (𝐁𝐈𝐋𝐋) 𝐃𝐄𝐓𝐀𝐈𝐋𝐒  ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟐 𝐓𝐎 𝐏𝐑𝐈𝐍𝐓 𝐒𝐎𝐂𝐈𝐄𝐓𝐘 (𝐁𝐈𝐋𝐋) 𝐃𝐄𝐓𝐀𝐈𝐋𝐒   ")
            print("✨ 𝐂𝐇𝐎𝐎𝐒𝐄 𝟑 𝐓𝐎 𝐄𝐗𝐈𝐓                      ")
            print("                                                    ")
            
            choice_1=int(input("ENTER CHOICE: "))
            
            if choice_1 == 1:
                welcome_message()  #Function Call
                print("<<<< 𝐇𝐎𝐔𝐒𝐈𝐍𝐆 (𝐁𝐈𝐋𝐋) 𝐃𝐄𝐓𝐀𝐈𝐋𝐒 >>>>")
                print('----------------------------------')
                cursor.execute("select * from housing_tax")
                data = cursor.fetchall()  #Fetch data command
                count = cursor.rowcount
                print("𝐓𝐨𝐭𝐚𝐥 𝐍𝐨. 𝐨𝐟 𝐑𝐨𝐰𝐬 𝐑𝐞𝐭𝐫𝐢𝐞𝐯𝐞𝐝 : ",count)
                print("|Owner ID | House ID | Maintenance | Electricity Bill|")

                for row in data:
                    print(row)
                    
            elif choice_1 == 2:
                welcome_message()  #Function Call
                
                print("<<<< 𝐒𝐎𝐂𝐈𝐄𝐓𝐘 (𝐁𝐈𝐋𝐋) 𝐃𝐄𝐓𝐀𝐈𝐋𝐒 >>>>")
                print('---------------------------------')
                cursor.execute("select * from societymain")
                data = cursor.fetchall()  #Fetch data command
                count = cursor.rowcount
                print("𝐓𝐨𝐭𝐚𝐥 𝐍𝐨. 𝐨𝐟 𝐑𝐨𝐰𝐬 𝐑𝐞𝐭𝐫𝐢𝐞𝐯𝐞𝐝 : ",count)
                print("|SNo | Month | Water Tax | Electricity Bill|")
                for row in data:
                    print('+++++++++++++++++++++++++++++++++++')
                    print('-----------------------------------')
                    print("Serial No. : ",row[0])
                    print('-----------------------------------')
                    print("Month: : ",row[1])
                    print('-----------------------------------')
                    print("Water Tax: : ",row[2])
                    print('-----------------------------------')
                    print("Electricity Bill : ",row[3])
                    print('-----------------------------------')
            
            elif choice_1 == 3:
                soc1 = 0   #While loop terminated
            
            else:
                print("++++++++++++++++++++++++++")
                print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
                print("++++++++++++++++++++++++++")
                     
    elif CHOICE == 10:
        exit()  #Function Call
        soc=0   #While loop terminated
      
    else:
        print("++++++++++++++++++++++++++")
        print("<<<< 𝐈𝐍𝐕𝐀𝐋𝐈𝐃 𝐂𝐇𝐎𝐈𝐂𝐄 ❗ >>>>") #INVALID CHOICE
        print("++++++++++++++++++++++++++")
        
        #END OF SOURCE CODE
        
        
            
