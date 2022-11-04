from tkinter import *
import sqlite3
import datetime
import time
from tkinter import messagebox

root = Tk()
root.title("Expense tracker")
#root.iconbitmap("favicon.ico")
root.geometry("440x500")
root.resizable(0,0)
#creating frames 
frame1 = Frame(root,bg="#ffe6e6")
frame1.pack(expand=True,fill="both")

frame2 = Frame(root,bg="#99e699")
frame2.pack(expand=True,fill="both")

frame3 = Frame(root,bg="#99e699")
frame3.pack(expand=True,fill="both")

frame4 = Frame(root,bg="#99e699")
frame4.pack(fill="both")

#Creating functions
def setBudget():
    a = budget.get()
    budget.delete(0,END)
    b = "Your budget is set as: $"+a
    budget.insert(0,b)

def add2c():
    global output
    #adding info to database
    #connect to database
    conn = sqlite3.connect("expensetrack.db")
    #create cursor
    curs = conn.cursor()
    #create table table name = SHOPLIST , (ITEM,QUANTITY,AMOUNT)
    curs.execute("INSERT INTO SHOPLIST VALUES(:date,:budget,:item,:quant,:amount)",
            {
                "date":date,
                "budget":budget.get(),
                "item":item.get(),
                "quant":quant.get(),
                "amount":amount.get()
            }
    )
    #commit database
    conn.commit()
    #close database
    conn.close()

    cost = int(quant.get())*int(amount.get())
    out = "Item: "+str(item.get())+" sum cost: "+str(cost)
    output = Checkbutton(frame2,text=out,bg="#99e699",font=("Franklin Gothic Medium",11),relief="flat")
    output.pack()

    item.delete(0,END)
    quant.delete(0,END)
    amount.delete(0,END)
'''   
def dList():
    deleted = Toplevel()
    deleted.title("delete entry")
    deleted.iconbitmap("favicon.ico")
    deleted.resizable(0,0)
    fram = Frame(deleted,bg="#ffccff")
    fram.pack(expand=True,fill="both")
    #creating labels 
    note = Label(fram,text="NOTE: ENTRIES WILL BE DELETED BY ITEM NAME",bg="#ffccff",relief="flat",font=("BalloonDExtBol",12))
    note.grid(row=0,column=0,columnspan=2)
    delId = Label(fram,text="Item Name:",bg="#ffccff",font=("Bahnschrift",11))
    delId.grid(row=1,column=0)
    #creating entry
    delIdE = Entry(fram,width=10)
    delIdE.grid(row=1,column=1,ipadx=10)
    
    #the delete function
    def delete():
        
        conn = sqlite3.connect("expensetrack.db")
        curs = conn.cursor()
        sql = "DELETE FROM SHOPLIST WHERE ITEM = "+ delIdE.get()
        curs.execute(sql)
        dlab = Label(fram,bg="#ffccff",text=f"item,{delIdE.get} has bee deleted",font=("CargoD",10))
        dlab.grid(row=5,column=1,ipadx=5,ipady=5)
        conn.commit()
        conn.close()

    #delete button
    delbtn = Button(fram,text="DELETE",bg="#ffccff",relief="flat",command=delete)
    delbtn.grid(row=2,column=1,columnspan=1,ipady=3,ipadx=5)
    #close buttoon
    clbtn = Button(fram,text="CLOSE",bg="#ffccff",relief="flat",command=deleted.destroy)
    clbtn.grid(row=3,column=1,ipadx=5,ipady=5)

    deleted.mainloop()
    '''
def vhistory():
    hist = Toplevel()
    #hist.resizable(0,0)
    #hist.iconbitmap("favicon.ico")
    hist.title("history viewer")
    hist.resizable(0,0)
    #creating window frame
    frame = Frame(hist,bg="#ffccff")
    frame.pack(expand=True,fill="both")
    #fetch data from data base
    conn = sqlite3.connect("expensetrack.db")
    curs = conn.cursor()
    sql = "SELECT *,oid FROM SHOPLIST"
    curs.execute(sql)
    records = curs.fetchall()
    prt_rec = " "
    for record in records:
        prt_rec += "Date: "+str(record[0])+ " ITEM: "+str(record[2])+"\n"
    out = Label(frame,text=prt_rec,bg="#ffccff",font=("Bahnschrift",12))
    out.grid(row=1,column=0,columnspan=2,pady=(5,0))
    conn.commit()
    conn.close()
    #definig clear history function
    def clear():
        conn = sqlite3.connect("expensetrack.db")
        curs = conn.cursor()
        curs.execute("DELETE FROM SHOPLIST;",)
        lbl = Label(frame,text=f'{curs.rowcount} items deleted!',bg="#ffccff")
        lbl.grid(row=3,column=1,padx=4,pady=4)
        conn.commit()
        conn.close()
        #response = messagebox.showwarning("DELETE HISTORY","THIS ACTIONS LEAVES THE DATABASE EMPTY")

    
    #delete history button
    btn  = Button(frame,text="clear history",relief="flat",bg="#ffccff",command=clear)
    btn.grid(row=3,column=0,ipadx=5,ipady=5)

    hist.mainloop()

def close():
    resp = messagebox.askyesno("close window","Are you sure you want to close window?")
    if resp == True:
        root.quit()

#create entry feild and label for estimsted budget
budg = Label(frame1,text="BUDGET:",bg="#ffe6e6",font=("Bahnschrift",12))
budg.grid(row=0,column=0)
budget = Entry(frame1,width=45)
budget.grid(row=0,column=1,ipadx=0,ipady=5)
btn = Button(frame1,text="SET",bg="#ffe6e6",command=setBudget,relief="flat")
btn.grid(row=1,column=1,columnspan=1,pady=5)

#create entry,label and button for items
name = Label(frame1,text="ITEM",bg="#ffe6e6",font=("Bahnschrift",8))
name.grid(row=2,column=0)
qty = Label(frame1,text="QUANTITY",bg="#ffe6e6",font=("Bahnschrift",8))
qty.grid(row=2,column=1)
amt = Label(frame1,text="AMOUNT",bg="#ffe6e6",font=("Bahnschrift",8))
amt.grid(row=2,column=2)
#Entries
item = Entry(frame1,width=10)
item.grid(row=3,column=0,ipadx=0,ipady=5)
quant = Entry(frame1,width=10)
quant.grid(row=3,column=1,ipadx=0,ipady=5)
amount = Entry(frame1,width=10)
amount.grid(row=3,column=2,ipadx=0,ipady=5)
#button
addBtn = Button(frame1,text="ADD TO CART",bg="#ffe6e6",relief="flat",command=add2c)
addBtn.grid(row=4,column=1,columnspan=1,pady=10)
#others
current_time = datetime.datetime.now()
date = current_time.strftime("%d/%m/%Y")
dateLabel = Label(frame1,text=date,font=("Bahnschrift",8),bg="#ffe6e6",relief="flat")
dateLabel.grid(row=5,column=2)
#veiw list and veiw history button
#dList = Button(frame1,text="DELETE LIST",relief="flat",bg="#ffe6e6",command=dList)
#dList.grid(row=5,column=0)
vhistory = Button(frame1,text="VEIW HISTORY",relief="flat",bg="#ffe6e6",command=vhistory)
vhistory.grid(row=5,column=1)
#close program button
closer = Button(frame4,text="close",bg="#99e699",command=close)
closer.pack(side="right")

root.mainloop()