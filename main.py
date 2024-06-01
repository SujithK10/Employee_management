from tkinter import *
from tkinter import ttk
from database import Database
from tkinter import messagebox

db=Database("EMPLOYEE.db")
root=Tk()
root.title("Employeee Management System")
root.geometry("1920x1080+0+0")#0,0 starts from x-axis =0,y-axis=0
root.config(bg="gray")
name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data['values']
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtadd.delete(1.0,END)
    txtadd.insert(END,row[7])

def Display_all():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_employee():
    if txtName.get()=="" or txtage.get()=="" or txtdoj.get()=="" or comboGender.get()=="" or txtcontact.get()=="" or txtem.get()=="" or txtadd.get(1.0,END)=="":
        messagebox.showerror("Error","FIll the valid details")
        return
    db.insert(txtName.get() , txtage.get(), txtdoj.get(), txtem.get(),comboGender.get(), txtcontact.get(), txtadd.get(1.0,END))
    messagebox.showinfo("Details ","Entered Successfully ")
    clear_all()
    Display_all()
def update_employee():
    if txtName.get()=="" or txtage.get()=="" or txtdoj.get()=="" or comboGender.get()=="" or txtcontact.get()=="" or txtem.get()=="" or txtadd.get(1.0,END)=="":
        messagebox.showerror("Error","FIll the valid details")
        return
    db.update(row[0],txtName.get() , txtage.get(), txtdoj.get(), txtem.get(),comboGender.get(), txtcontact.get(), txtadd.get(1.0,END))
    messagebox.showinfo("Details ","Updated Successfully ")
    clear_all()
    Display_all()
def delete_employee():
    db.remove(row[0])
    clear_all()
    Display_all()
def clear_all():
    name.set("")
    age .set("")
    doj.set("")
    gender.set("")
    email .set("")
    contact.set("")
    txtadd.delete(1.0,END)

#Entry Frame
enteries_Frame=Frame(root,bg="#535c68")
enteries_Frame.pack(side=TOP,fill=X)
title=Label(enteries_Frame,text="Employee Management system",font=("calibri",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblName=Label(enteries_Frame,text="Name",font=("calibri",12,),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(enteries_Frame,textvariable=name,font=("calibri",12,),width=25)
txtName.grid(row=1,column=1,padx=10,sticky="w")

lblage=Label(enteries_Frame,text="Age",font=("calibri",12,),bg="#535c68",fg="white")
lblage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtage=Entry(enteries_Frame,textvariable=age,font=("calibri",12,),width=25)
txtage.grid(row=1,column=3,padx=10,sticky="w")

lbldoj=Label(enteries_Frame,text="D.O.J",font=("calibri",12,),bg="#535c68",fg="white")
lbldoj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtdoj=Entry(enteries_Frame,textvariable=doj,font=("calibri",12,),width=25)
txtdoj.grid(row=2,column=1,padx=10,sticky="w")

lblem=Label(enteries_Frame,text="Email",font=("calibri",12,),bg="#535c68",fg="white")
lblem.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtem=Entry(enteries_Frame,textvariable=email,font=("calibri",12,),width=25)
txtem.grid(row=2,column=3,padx=10,sticky="w")

lblGender=Label(enteries_Frame,text="Gender",font=("calibri",12,),bg="#535c68",fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGender=ttk.Combobox(enteries_Frame,textvariable=gender,font=("calibri",12,),width=23,state="readyonly")
comboGender['values']=("Male","Female")
comboGender.grid(row=3,column=1,padx=10,sticky="w")

lblcontact=Label(enteries_Frame,text="Contact",font=("calibri",12,),bg="#535c68",fg="white")
lblcontact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtcontact=Entry(enteries_Frame,textvariable=contact,font=("calibri",12,),width=25)
txtcontact.grid(row=3,column=3,padx=10,sticky="w")

lblAddress=Label(enteries_Frame,text="Address",font=("calibri",12,),bg="#535c68",fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtadd=Text(enteries_Frame,width=85,height=1,font=("calibri",12,))
txtadd.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")
#Buttons
Btn_frame=Frame(enteries_Frame,bg='#535c68')
Btn_frame.grid(row=6,column=0,padx=10,columnspan=4,pady=10,sticky="w")
btnAdd=Button(Btn_frame,command=add_employee,text="Add Details",width=15,font=("calibri",10,"bold"),bg="#16a085",fg="white",bd=0).grid(row=0,column=0,padx=10)


btnupdate=Button(Btn_frame,command=update_employee,text="Update Details",width=15,font=("calibri",10,"bold"),bg="#2980b9",fg="white",bd=0).grid(row=0,column=1,padx=10)


btndel=Button(Btn_frame,command=delete_employee,text="Delete Details",width=15,font=("calibri",10,"bold"),bg="#c0392b",fg="white",bd=0).grid(row=0,column=2,padx=10)


btnclear=Button(Btn_frame,command=clear_all,text="Clear All",width=15,font=("calibri",10,"bold"),bg="#f39c12",fg="white",bd=0).grid(row=0,column=3,padx=10)


#TABLE FRAME
tree_frame=Frame(root,bg="#ecf0f1")
tree_frame.place(x=0,y=320,width=1275,height=520)
style=ttk.Style()
style.configure("mysytle.Treeview",font=('calibri',14),rowheight=40)

tv=ttk.Treeview(tree_frame,column=(1,2,3,4,5,6,7,8),style="mysytle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.column("2",width=30)
tv.heading("3",text="Age")
tv.column("3",width=5)
tv.heading("4",text="D.O.J")
tv.column("4",width=12)
tv.heading("5",text="Email")

tv.heading("6",text="Gender")
tv.column("6",width=10)
tv.heading("7",text="Contact")
tv.column("7",width=28)
tv.heading("8",text="Address")

tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

Display_all()
root.mainloop()