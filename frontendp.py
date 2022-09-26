#frontend
from tkinter import *
import tkinter.messagebox
import dbbackend
class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Database")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="Ghost White")
        SDS = StringVar()
        Name = StringVar()
        LEI = StringVar()
        Email = StringVar()
        Tel = StringVar()
        Sales = StringVar()
        Parent = StringVar()
        Notes = StringVar()
        def iExit():
            iExit = tkinter.messagebox.askyesno("Database", "Confirm if you want to exit")

            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtSDS.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtTel.delete(0, END)
            self.txtSales.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtNotes.delete(0, END)

        def addData():
            if len(SDS.get()) != 0:
                dbbackend.addStdRec(SDS.get(), Name.get(), LEI.get(), Email.get(), Tel.get(), Sales.get(), Parent.get(), Notes.get())

                studentlist.delete(0, END)
                studentlist.insert(END, (SDS.get(), Name.get(), LEI.get(), Email.get(), Tel.get(), Sales.get(), Parent.get(), Notes.get()))

        def DisplayData():
            studentlist.delete(0, END)
            for row in dbbackend.viewData():
                studentlist.insert(END, row, "")

        def StudentRec(event):
            global sd
            searchStd = studentlist.curselection()[0]
            sd = studentlist.get(searchStd)
            self.txtSDS.delete(0, END)
            self.txtSDS.insert(END, sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END, sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END, sd[4])
            self.txtTel.delete(0, END)
            self.txtTel.insert(END, sd[5])
            self.txtSales.delete(0, END)
            self.txtSales.insert(END, sd[6])
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END, sd[7])
            self.txtNotes.delete(0, END)
            self.txtNotes.insert(END, sd[8])

        def DeleteData():
            if len(SDS.get()) != 0:
                dbbackend.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            studentlist.delete(0, END)
            for row in dbbackend.searchData(SDS.get(), Name.get(), LEI.get(), Email.get(), Tel.get(), Sales.get(), Parent.get(), Notes.get()):
                studentlist.insert(END, row, "")

        def update():
            if len(SDS.get()) != 0:
                dbbackend.deleteRec(sd[0])
            if len(SDS.get()) != 0:
                dbbackend.addStdRec(SDS.get(), Name.get(), LEI.get(), Email.get(), Tel.get(), Sales.get(), Parent.get(), Notes.get())

                studentlist.delete(0, END)
                studentlist.insert(END, (SDS.get(), Name.get(), LEI.get(), Email.get(), Tel.get(), Sales.get(), Parent.get(), Notes.get()))

        MainFrame = Frame(self.root, bg="Ghost White")
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2, padx=54, pady=8, bg="Ghost White", relief=RIDGE)

        TitFrame.pack(side=TOP)
        self.lblTit = Label(TitFrame, font=('times new roman', 48, 'bold'), text="Database", bg="Ghost White")

        self.lblTit.grid()
        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg="Ghost White", relief=RIDGE)

        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE, bg="Ghost White")

        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg="Ghost White", font=('times new roman', 26, 'bold'))

        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE, bg="Ghost White", font=('times new roman', 20, 'bold'))

        DataFrameRIGHT.pack(side=RIGHT)
        self.lblSDS = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="SDS:", padx=2, pady=2, bg="Ghost White")

        self.lblSDS.grid(row=0, column=0, sticky=W)
        self.txtSDS = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=SDS, width=39)

        self.txtSDS.grid(row=0, column=1)
        self.lblfna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Name:", padx=2, pady=2, bg="Ghost White")

        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Name, width=39)

        self.txtfna.grid(row=1, column=1)
        self.lblSna = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="LEI:", padx=2, pady=2, bg="Ghost White")

        self.lblSna.grid(row=2, column=0, sticky=W)
        self.txtSna = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=LEI, width=39)

        self.txtSna.grid(row=2, column=1)
        self.lblDoB = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Email:", padx=2, pady=2, bg="Ghost White")

        self.lblDoB.grid(row=3, column=0, sticky=W)
        self.txtDoB = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Email, width=39)

        self.txtDoB.grid(row=3, column=1)
        self.lblTel = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Tel:", padx=2, pady=2, bg="Ghost White")

        self.lblTel.grid(row=4, column=0, sticky=W)
        self.txtTel = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Tel, width=39)

        self.txtTel.grid(row=4, column=1)
        self.lblSales = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Sales:", padx=2, pady=2, bg="Ghost White")

        self.lblSales.grid(row=5, column=0, sticky=W)
        self.txtSales = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Sales, width=39)

        self.txtSales.grid(row=5, column=1)
        self.lblAdr = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Parent:", padx=2, pady=2, bg="Ghost White")

        self.lblAdr.grid(row=6, column=0, sticky=W)
        self.txtAdr = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Parent, width=39)

        self.txtAdr.grid(row=6, column=1)
        self.lblNotes = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Notes:", padx=2, pady=2, bg="Ghost White")

        self.lblNotes.grid(row=7, column=0, sticky=W)
        self.txtNotes = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=Notes, width=39)

        self.txtNotes.grid(row=7, column=1)
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')
        studentlist = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'), yscrollcommand=scrollbar.set)

        studentlist.bind('<<ListboxSelect>>', StudentRec)
        studentlist.grid(row=0, column=0, padx=8)
        scrollbar.config(command=studentlist.yview)
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=addData)

        self.btnAddData.grid(row=0, column=0)
        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)

        self.btnDisplayData.grid(row=0, column=1)
        self.btnClearData = Button(ButtonFrame, text="Clear", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=clearData)

        self.btnClearData.grid(row=0, column=2)
        self.btnDeleteData = Button(ButtonFrame, text="Delete", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=DeleteData)

        self.btnDeleteData.grid(row=0, column=3)
        self.btnSearchData = Button(ButtonFrame, text="Search", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=searchDatabase)

        self.btnSearchData.grid(row=0, column=4)
        self.btnUpdateData = Button(ButtonFrame, text="Update", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=update)

        self.btnUpdateData.grid(row=0, column=5)
        self.btnExit = Button(ButtonFrame, text="Exit", font=('times new roman', 20, 'bold'), height=1, width=10, bd=4, command=iExit)

        self.btnExit.grid(row=0, column=6)

if __name__=='__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()
