import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testdb"
)

#from	datetime import datetime
#now=datetime.now()
#DJ=now.strftime('%Y-%m-%d %H:%M:%S')
i=10000
while(True):
	try:
		print("\n                             ")
		print("\n```````````````````````````````````````````````````````````````````````````")
		print("\n                    S-TECHNOLOGY STUDENT MANAGEMENT SYSTEM           ")
		print("\n```````````````````````````````````````````````````````````````````````````")
		print("\n             1.     :     Login")
		print("\n             2.     :     New user")
		z=int(input("\n         Enter the choice "))
	except:
		print("press any of the above")
		continue
	if(z==1):
		print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("\n|||||||||||||||||||||||||||||||||")
		print("\n            Login Page")
		print("\n                                 ")
		x=input("           User name   :")
		if x=="":
			print("\n       Null value not accepted      ")
			break
		else:	
			mycursor = mydb.cursor()
			mycursor.execute("SELECT User_Name from users where User_Name ='"+x+"'")
			myresult=mycursor.fetchone()
			#print(myresult)
			if myresult:
				y=input("           Password    :")
				mycursor.execute("SELECT Password from users where User_Name ='"+x+"' AND Password ='"+str(y)+"'")
				myresult=mycursor.fetchone()
				if myresult:
					print("\n       successfully Logged in....!!!!!!!...Welcome back")
				else:
					print("\n       Incorrect password ")
					break
			else:
				print("\n     user name not in db")
				print("\n          Create new user")
				print("\n~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~|~")
				x=input("       User name   :      ")
				if x=="":
					print("\n             Null value not accepted")
					break
				else:
					if myresult:
						print("\n User name already exist")
						break
					else:	
						y=input("       Password    :")
						sql = "INSERT INTO USERS (User_Name, Password) VALUES (%s, %s)"
						val = (x,y)
						mycursor.execute(sql, val)
						mydb.commit()
						print("\n")
						print("User successfully created.")
	elif(z==2):
		print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print("\n|||||||||||||||||||||||||||||||||")
		print("\n            Create new user")
		print("\n                                 ")
		x=input("       User name   :")
		mycursor.execute("SELECT User_Name from users where User_Name ='"+x+"'")
		myresult=mycursor.fetchone()
		if myresult:
			print("\n     User name already exist")
		else:	
			y=input("      Password    :")
			sql = "INSERT INTO USERS (User_Name, Password) VALUES (%s, %s)"
			val = (x,y)
			mycursor.execute(sql, val)
			mydb.commit()
			print("\n")
			print("User successfully created.")
	else:
		print("\n invalid choice")
		break	

		
	while(True):	
		print("\n-----------------------------------------------")	
		print("\n                     Main Menu")
		print("\n-----------------------------------------------")
		print("\n     1     :     Add Student Details")
		print("\n     2     :     View Student details")
		print("\n     3     :     Update Fee Details")
		print("\n     4     :     Delete Student")
		print("\n     5     :     Exit")
		try:
			w=int(input("\n          Select you choice "))
		except:
			print("\n                Select one of the above to continue     ")
			continue	
		if(w==1):
			print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("\n               S-TECHNOLOGY")
			print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
			print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			print("\n               Student Admission Form")
			print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
			adnum=True
			while (adnum):
				try:
					AN=int(input("\n             Admission Number    :     "))
				except:
					print("\n Enter number to continue     ")
					continue	
				mycursor=mydb.cursor()
				mycursor.execute("SELECT Admission_Number from students where Admission_Number='"+str(AN)+"'")
				myresult = mycursor.fetchone()
				#mydb.commit()
				
				if myresult:
					print("\n        Admission number already exist   ")
					continue
						
				else:	
					adnum=False

				N=input("\n               Name               :     ")
				try:
					AG=int(input("\n               Age                 :     "))
				except:
					print("\nEnter Age to continue")
					continue	
				GE=input("\n               Gender              :     ")
				AD=input("\n               Address             :     ")
				try:
					MN=input("\n         Mobile Number      :     ")
				except:
					print("\nEnter numbers to continue")
					continue
				print("\n************Course Details************")
				CO=input("\n            Course                 :     ")
				DJ=input("\n            Date Joined            :     ")
				CD=input("\n            Course_duration        :     ")
				TF=int(input("\n            Total_fees             :     "))
				feepaid=True
				while (feepaid):
					try:
						FP=int(input("\n            Fees_paid              :     "))
					except:
						print("\n      Enter Fees_paid")	
						continue
					if FP<i:
						print("\n             Minimun amount should be 10000")
						continue
					else:
						feepaid=False
						FPD=input("\n           Fees_paid_date         :     ")
						BA=int(input("\n             Balance               :     "))
						
							#FP=int(input("\n      Enter the amount "))
							#FPD=input("\n           Fees_paid_date         :     ")
							#BA=int(input("\n             Balance               :     "))
				

			mycursor=mydb.cursor()
			sql1="INSERT INTO Students(Admission_Number, Name, Age, Gender, Address, Mobile_Number) VALUES(%s, %s, %s, %s, %s, %s)"
			val1=(AN, N, AG, GE, AD, MN)
			mycursor.execute(sql1, val1)
			mydb.commit()

			mycursor=mydb.cursor()
			sql3="INSERT INTO Course(Course_D, Date_joined, Course_duration, Total_Fee, Fees_paid, 1st_date, Balance) VALUES(%s, %s, %s, %s, %s, %s, %s)"
			val3=(CO, DJ, CD, TF, FP, FPD, BA)
			mycursor.execute(sql3, val3)
			mydb.commit()

			mycursor=mydb.cursor()
			sql2="UPDATE course SET Admission_Number='"+str(AN)+"'where Admission_Number ='""'"
			mycursor.execute(sql2)
			mydb.commit()
			print("\n==============================Record inserted=======================")
			mycursor=mydb.cursor()
			sql2="UPDATE course SET 1st_installment='"+str(FP)+"'where Admission_Number ='"+str(AN)+"'"
			mycursor.execute(sql2)
			mydb.commit()

			#mycursor=mydb.cursor()
			#mycursor.execute("SELECT Admission_Number from Course")
			if FP==TF:
				mycursor=mydb.cursor()
				mycursor.execute("UPDATE course set Fee_status='complete' where Admission_Number='"+str(AN)+"'")
				mydb.commit()
			else:
				mycursor=mydb.cursor()
				mycursor.execute("UPDATE course set Fee_status='incomplete'where Admission_Number='"+str(AN)+"'")
				mydb.commit()
			#mycursor.execute("SELECT Admission_Number from Students where Admission_Number='"+AN+"'")
			
			
		elif(w==2):
			a=input("\nEnter Admission number ")
			mycursor=mydb.cursor()
			mycursor.execute("SELECT * FROM students where Admission_Number = '"+str(a)+"' ")
			myresult = mycursor.fetchall()
			mydb.commit()
			mycursor=mydb.cursor()
			mycursor.execute("SELECT * FROM course where Admission_Number='"+str(a)+"'")
			myresult1 = mycursor.fetchall()
			mydb.commit()

			if myresult:			
				for row in myresult:
					print("\n===============================Student Details==================================")
					print("\n--------------------------------------------------------------------------------")	
					print("\n                    Admission_Number      =         ",row[0])
					print("                    Name                  =         ",row[1])
					print("                    Age                   =         ",row[2])
					print("                    Gender                =         ",row[3])
					print("                    Address               =         ",row[4])
					print("                    Mobile number         =         ",row[5])
				for z in myresult1:
					print("                    Course                =         ",z[1])
					print("                    Date joined           =         ",z[2])
					print("                    Course duration       =         ",z[3])
					print("                    Total fee             =         ",z[4])
					print("                    Fees_paid             =         ",z[5])
					print("                    1st installment       =         ",z[6])
					print("                    1st installment date  =         ",z[7])
					print("                    2nd installment       =         ",z[8])
					print("                    2nd installment date  =         ",z[9])
					print("                    Balance               =         ",z[10])	
					print("                    Fee status            =         ",z[11])
			else:
				print("\n     Admission number not in records")

		#update fee details	
		elif(w==3):
			try:
				a=int(input("\n Enter the admission number "))
			except:
				print("\n      Enter admission number to continue")
				continue	
			mycursor=mydb.cursor()
			mycursor.execute("SELECT Admission_Number,Course_D,Total_Fee,Fees_paid,Balance FROM course where Admission_Number='"+str(a)+"'")
			myresult=mycursor.fetchall()
			mydb.commit()
			if myresult:
				for x in myresult:
					print("\n                   Admission_number =        ",x[0])
					print("                   course           =        ",x[1])
					print("                   Total_fees       =        ",x[2])
					print("                   Fees paid        =        ",x[3])
					print("                   Balance Amount   =        ",x[4])
				b=int(x[4])#Balance amount
				c=int(x[3])#Fees paid
				d=int(x[2])#total fees
				if b==0:
					print("\n fee status completed")
					break
				else:
					fpstatus=True
					while(fpstatus):	
						y=int(input("\n Enter the amount to enter "))
						if y!=b:
							print("\n                unable to make payment")
							print("\n                Enter the balance amount to continue=",b)
							
							#if FP==d:
							#mycursor=mydb.cursor()
							#mycursor.execute("UPDATE course set Fee_status='complete',Balance='0' where Admission_Number='"+str(a)+"'")
							#mydb.commit()
						else:
							fpstatus=False
							z=input("\n Enter the date ")
							FP=c+y
							mycursor=mydb.cursor()
							mycursor.execute("UPDATE course set Fees_paid ='"+str(FP)+"',2nd_installment='"+str(y)+"', 2nd_Date ='"+str(z)+"' where Admission_Number='"+str(a)+"'")
							mydb.commit()
							print("\n Fees_paid updated")
							#y=int(input("\n          Enter the amount      :               "))
							#z=input("\n              Enter the date        :                ")
							#FP=c+y
							#mycursor=mydb.cursor()
							#mycursor.execute("UPDATE course set Fees_paid ='"+str(FP)+"',2nd_installment='"+str(y)+"', 2nd_Date ='"+str(z)+"' where Admission_Number='"+str(a)+"'")
							#mydb.commit()
							#print("\n Fees_paid updated")
							mycursor=mydb.cursor()
							mycursor.execute("UPDATE course set Fee_status='complete',Balance='0' where Admission_Number='"+str(a)+"'")
							mydb.commit()

			else:
				print("\n                           Not in records")		
		elif(w==4):
			try:
				a=int(input("\n                       Enter the admission number "))
			except:
					print("\n                         Enter admission number to continue")
					continue		
			mycursor=mydb.cursor()
			mycursor.execute("SELECT * FROM course where Admission_Number='"+str(a)+"'")
			myresult=mycursor.fetchall()
			if myresult:
				mycursor=mydb.cursor()
				mycursor.execute("DELETE FROM students where Admission_Number = '"+str(a)+"'")
				mydb.commit()
				mycursor=mydb.cursor()
				mycursor.execute("DELETE FROM course where Admission_Number = '"+str(a)+"'")
				mydb.commit()
				print("\n              Record deleted")
			else:
				print("\n              Admission number not in records")

		elif(w==5):
			exit()

		else:
			print("\n                Please enter correct choice")	

