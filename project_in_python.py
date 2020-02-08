from tkinter  import *
import datetime
from mypeople import MyPeople
from addpeople import AddPeople
from About_us import  About
date=datetime.datetime.now().date()
date=str(date)

class Application(object):
	def __init__(self,master):
		self.master=master


		#frames

		self.top=Frame(master,height=150,bg='white')
		self.top.pack(fill=X)



		self.bottom=Frame(master,height=500,bg='#34baeb')
		self.bottom.pack(fill=X)


		#top frame design
		self.top_image=PhotoImage(file='C://Users//Dell//Desktop//phonebook//icons//phone.png')
		
		self.top_image_label=Label(self.top, image=self.top_image)
		self.top_image_label.place(x=120,y=30)


		self.heading=Label(self.top,text='My Phonebook App',font='arial 15 bold',bg='white',fg='#ebb434')
		self.heading.place(x=230,y=50 )


		self.date_lbl=Label(self.top,text="Today's Date"+date, font='arial 12 bold',fg='#ebb434',bg='white')
		self.date_lbl.place(x=450,y=110)



		#button1 view prople
		self.viewButton=Button(self.bottom,text="   My People   ",font='arial  12 bold',command=self.my_people)
		self.viewButton.place(x=260,y=70)



		#button2  add people
		self.addButton=Button(self.bottom,text="  Add People  ",font='arial  12 bold',command=self.addpeoplefunction)
		self.addButton.place(x=260,y=130)





		#button3  about us
		self.aboutButton=Button(self.bottom,text="    About us     ",font='arial  12 bold',command=self.about_us)
		self.aboutButton.place(x=260,y=190)


	def my_people(self):
		people=MyPeople()

	def about_us(self):
		aboutpage=About()
		
				

	def addpeoplefunction(self):
		addpeoplewindow=AddPeople()












def main():
	root=Tk()
	app=Application(root)
	root.title("Phonebook App")
	root.geometry("650x550+350+200")
	root.resizable(False,False)
	root.mainloop()




if __name__ =='__main__':
	main()