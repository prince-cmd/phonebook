from tkinter import *
import sqlite3
from tkinter import messagebox

con=sqlite3.connect('database.db')
cur=con.cursor()



class AddPeople(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)

		self.geometry("650x650+600+200")
		self.title("Add New Person")
		self.resizable(False,False)

		self.top=Frame(self,height=150,bg='white')
		self.top.pack(fill=X)



		self.bottom=Frame(self,height=500,bg='#fcd79c')
		self.bottom.pack(fill=X)


		#top frame design
		self.top_image=PhotoImage(file='C://Users//Dell//Desktop//phonebook//icons//single.png')
		
		self.top_image_label=Label(self.top, image=self.top_image)
		self.top_image_label.place(x=120,y=30)


		self.heading=Label(self.top,text='Add New Person ',font='arial 15 bold',bg='white')
		self.heading.place(x=260,y=50 )


		#name 
		self.label_name=Label(self.bottom,text="Name",font='arial 15 bold',fg='white',bg='#fcc324')
		self.label_name.place(x=40,y=40)


		self.entry_name=Entry(self.bottom,width=30,bd=4)
		self.entry_name.insert(0,"Enter Name")
		self.entry_name.place(x=150,y=40)
		#surname

		self.label_surname=Label(self.bottom,text="Surname",font='arial 15 bold',fg='white',bg='#fcc324')
		self.label_surname.place(x=40,y=80)


		self.entry_surname=Entry(self.bottom,width=30,bd=4)
		self.entry_surname.insert(0,"Enter Surname")
		self.entry_surname.place(x=150,y=80)




		#email
		self.label_email=Label(self.bottom,text="Email",font='arial 15 bold',fg='white',bg='#fcc324')
		self.label_email.place(x=40,y=120)


		self.entry_email=Entry(self.bottom,width=30,bd=4)
		self.entry_email.insert(0,"Enter Email")
		self.entry_email.place(x=150,y=120)




		#phonenumber
		self.label_phone=Label(self.bottom,text="Phone No.",font='arial 15 bold',fg='white',bg='#fcc324')
		self.label_phone.place(x=40,y=160)


		self.entry_phone=Entry(self.bottom,width=30,bd=4)
		self.entry_phone.insert(0,"Enter Surname")
		self.entry_phone.place(x=150,y=160)



		#address

		self.label_address=Label(self.bottom,text="Address",font='arial 15 bold',fg='white',bg='#fcc324')
		self.label_address.place(x=40,y=200)


		self.entry_address=Text(self.bottom,width=32,height=5)
		
		self.entry_address.place(x=150,y=200)



		#button
		button=Button(self.bottom,text="Confirm",command=self.add_people)
		button.place(x=270,y=460)



	def add_people(self):
		name=self.entry_name.get()
		surname=self.entry_surname.get()
		email=self.entry_email.get()
		phone=self.entry_phone.get()
		address=self.entry_address.get(1.0,'end-1c')


		if name and surname and email and phone and address !="":
			try:
				#add to the database
				query="insert into  'addressbook'(person_name,person_surname,person_email,person_phone,person_address) values (?,?,?,?,?)"
				cur.execute(query, (name,surname,email,phone,address))
				con.commit()
				messagebox.showinfo("Success","Contact Added")
			except EXCEPTION as e:
				messagebox.showerror("Error",str(e))

			



		else:
			messagebox.showerror("Error","Fill the all the fields",icon='warning')
		





























