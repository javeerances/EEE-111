from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from SDSqlite import SDSqlite
import tkinter as tk
import csv

class SDGUI(Tk):
        def __init__(self, SDData=SDSqlite("AppSD.db")):
                super().__init__()
                self.SDB = SDData

                self.title("High School Database")
                self.geometry("1400x750")
                self.resizable(False, False)
                self.config(bg="#0A043C")
                self.style = ttk.Style()

                #Label HIGH SCHOOL DATABASE Set-up
                self.bg = Label(self,
                        text="",
                        bg="#EADBC8",
                        height=6,
                        width=900,
                        )
                self.bg.place(x=0, y=0)

                self.heading = Label(self,
                                text="HIGH SCHOOL DATABASE",
                                font=("Tw Cen MT Condensed Extra Bold", 27),
                                bg="#EADBC8",
                                fg="#0A043C"
                                )
                self.heading.place(x=35, y=25)

                #Treeview Set-up
                self.style.theme_use("default")
                self.style.configure('Treeview', 
                                font=("Tw Cen MT Condensed Extra Bold", 15), 
                                foreground='#0A043C',
                                background='#EADBC8',
                                fieldbackground='#EADBC8',
                                rowheight= 45
                                )

                self.style.configure("Treeview.Heading", 
                                foreground="#EADBC8",
                                background="#0A043C",
                                font= ("Tw Cen MT Condensed Extra Bold", 20),
                                )

                self.style.map('Treeview',
                        background=[('selected', '#0A043C')],
                        foreground=[('selected', '#EADBC8')]
                        )

                self.tree = ttk.Treeview(self)
                self.tree["columns"] = ("Student No.",
                                "Name",
                                "Email Address",
                                "Name of School",
                                "Region"
                                )

                self.tree.column("#0", width=0, stretch=NO),
                self.tree.column("Student No.", anchor=CENTER, width=150)
                self.tree.column("Name", anchor=CENTER, width=150)
                self.tree.column("Email Address", anchor=CENTER, width=170)
                self.tree.column("Name of School", anchor=CENTER, width=250)
                self.tree.column("Region", anchor=CENTER, width=100)

                self.tree.heading("#0", text="\n")
                self.tree.heading("Student No.", text="Student No.")
                self.tree.heading("Name", text="Name")
                self.tree.heading("Email Address", text="Email Address")
                self.tree.heading("Name of School", text="Name of School")
                self.tree.heading("Region", text="Region")

                self.tree.place(x=450,
                        y=60,
                        width=900,
                        height=620,
                        )
                self.tree.bind('<ButtonRelease>', self.readdata)
                self.addTreeview

                #Student No. Set-up
                self.SNvalue = StringVar()
                self.StudentNo = Label(self,
                                text="STUDENT NO:",
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#0A043C",
                                fg="#EADBC8"
                                )
                self.StudentNo.place(x=50, y=130)
                self.SNentry= Entry(self,
                        font=("Tw Cen MT Condensed Extra Bold", 15),
                        width=30,
                        bg="#FDF0F0",
                        fg="#0A043C",
                        textvariable=self.SNvalue
                        )
                self.SNentry.place(x=53, y=165)

                #Name Set-up
                self.Nvalue = StringVar()
                self.Name = Label(self,
                                text="NAME:",
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#0A043C",
                                fg="#EADBC8"
                                )
                self.Name.place(x=50, y=200)
                self.Naentry= Entry(self,
                        font=("Tw Cen MT Condensed Extra Bold", 15),
                        width=30,
                        bg="#FDF0F0",
                        fg="#0A043C",
                        textvariable=self.Nvalue
                        )
                self.Naentry.place(x=53, y=235)

                #E-mail Set-up
                self.Evalue = StringVar()
                self.Email = Label(self,
                                text="EMAIL ADDRESS:",
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#0A043C",
                                fg="#EADBC8"
                                )
                self.Email.place(x=50, y=270)
                self.Ementry= Entry(self,
                        font=("Tw Cen MT Condensed Extra Bold", 15),
                        width=30,
                        bg="#FDF0F0",
                        fg="#0A043C",
                        textvariable=self.Evalue
                        )
                self.Ementry.place(x=53, y=305)

                #School Set-up
                self.Svalue = StringVar()
                self.School = Label(self,
                                text="NAME OF SCHOOL:",
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#0A043C",
                                fg="#EADBC8"
                                )
                self.School.place(x=50, y=340)
                self.Schentry= Entry(self,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                width=30,
                                bg="#FDF0F0",
                                fg="#0A043C",
                                textvariable=self.Svalue
                                )
                self.Schentry.place(x=53, y=375)

                #Region Set-up
                self.Region = Label(self,
                                text="REGION:",
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#0A043C",
                                fg="#EADBC8"
                                )
                self.Region.place(x=50, y=410)
                self.regions =["Region I",
                        "Region II",
                        "Region III",
                        "Region IV-A",
                        "Region IV-B",
                        "Region V",
                        "Region VI",
                        "Region VII",
                        "Region VIII",
                        "Region IX",
                        "Region X",
                        "Region XI",
                        "Region XII",
                        "Region XIII",
                        "CAR",
                        "NCR",
                        "BARMM",
                        "International"
                        ]
                self.Rvalue = StringVar()
                self.Rvalue.set(self.regions[0])
                self.RGdropbox = OptionMenu(self,
                                self.Rvalue,
                                *self.regions,
                                )
                self.RGdropbox.configure(width=32, 
                                font=("Tw Cen MT Condensed Extra Bold", 12),
                                bg="#FDF0F0",
                                fg="#0A043C"
                                )
                self.RGdropbox.place(x=53, y=445)

                #Button1 New Set-up
                self.NewButton = Button(self,
                                text="New School",
                                width=32,
                                height=1,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#FDF0F0",
                                fg="#0A043C",
                                command=lambda:self.cleardata(True)
                                )
                self.NewButton.place(x=53, y=520)

                #Button2 New School Set-up
                self.AddButton = Button(self,
                                text="Add School",
                                width=32,
                                height=1,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#FDF0F0",
                                fg="#0A043C",
                                command=self.adddata
                                )
                self.AddButton.place(x=53, y=570)

                #Button3 Remove Set-up
                self.RemoveButton = Button(self,
                                text="Remove School",
                                width=32,
                                height=1,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#FDF0F0",
                                fg="#0A043C",
                                command=self.deletedata
                                )
                self.RemoveButton.place(x=53, y=620)

                #Button4 Remove Set-up
                self.UpdateButton = Button(self,
                                text="Update School",
                                width=32,
                                height=1,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#FDF0F0",
                                fg="#0A043C",
                                command=self.updatedata
                                )
                self.UpdateButton.place(x=53, y=670)

                #Button5 Export CSV Set-up
                self.ExportcsvButton = Button(self,
                                text="Export to CSV",
                                width=32,
                                height=1,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#FDF0F0",
                                fg="#0A043C",
                                command=self.exportedcsv
                                )
                self.ExportcsvButton.place(x=730, y=695)

                #Button6 Export JSON Set-up
                self.ExportjsonButton = Button(self,
                                text="Export to JSON",
                                width=32,
                                height=1,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#FDF0F0",
                                fg="#0A043C",
                                command=self.exportedjson
                                )
                self.ExportjsonButton.place(x=1050, y=695)

                #Button7 Import CSV Set-up
                self.importcsvButton = Button(self,
                                text="Open File",
                                width=32,
                                height=1,
                                font=("Tw Cen MT Condensed Extra Bold", 15),
                                bg="#FDF0F0",
                                fg="#0A043C",
                                command=self.importedcsv
                                )
                self.importcsvButton.place(x=1050, y=10)
        
        def addTreeview(self):
                students = self.SDB.compiledata()
                self.tree.delete(*self.tree.get_children())
                for student in students:
                        print(student)
                        self.tree.insert('', END, values=student)
        
        def cleardata(self, *clicked):
                if clicked:
                        self.tree.selection_remove(self.tree.focus())
                        self.tree.focus('')
                self.SNvalue.set('')
                self.Nvalue.set('')
                self.Evalue.set('')
                self.Svalue.set('')
                self.Rvalue.set('Region I')

        def readdata(self, event):
                clicked = self.tree.focus()
                if clicked:
                        row = self.tree.item(clicked)['values']
                        self.cleardata()
                        self.SNvalue.set(row[0])
                        self.Nvalue.set(row[1])
                        self.Evalue.set(row[2])
                        self.Svalue.set(row[3])
                        self.Rvalue.set(row[4])
                else:
                        pass
        
        def adddata(self):
                studentno = self.SNvalue.get()
                name = self.Nvalue.get()
                email = self.Ementry.get()
                school = self.Svalue.get()
                region = self.Rvalue.get()

                if not(studentno and name and email and school and region):
                        messagebox.showerror("Error", "Fill all the boxes.")
                elif self.SDB.studentexists(studentno):
                        messagebox.showerror("Error", "Student No. already exists.")
                else:
                        self.SDB.addschool(studentno, name, email, school, region)
                        self.addTreeview()
                        self.cleardata
                        messagebox.showinfo("Success", "Data has been added.")
        
        def deletedata(self):
                clicked = self.tree.focus()
                if not clicked:
                        messagebox.showerror("Error", "Choose a data to delete")
                else:
                        studentno = self.SNvalue.get()
                        self.SDB.deleteschool(studentno)
                        self.addTreeview()
                        self.cleardata
                        messagebox.showinfo("Success", "Data has been removed.")

        def updatedata(self):
                clicked = self.tree.focus()
                if not clicked:
                        messagebox.showerror("Error", "Choose a data to update")
                else: 
                        studentno = self.SNvalue.get()
                        name = self.Nvalue.get()
                        email = self.Evalue.get()
                        school = self.Svalue.get()
                        region = self.Rvalue.get()
                        self.SDB.updateschool(studentno, name, email, school, region)
                        self.addTreeview()
                        self.cleardata()
                        messagebox.showinfo("Success", "Data has been updated")
        
        def exportedcsv(self):
                self.SDB.exportcsv()
                messagebox.showinfo("Success", f'Data has been exported to{self.SDB.SDName}')

        def exportedjson(self):
                self.SDB.exportjson()
                messagebox.showinfo("Success", f'Data has been exported to SchoolDB.json')

        def importedcsv(self):
                path = tk.filedialog.askopenfilename(filetypes=[('CSV Files','*.csv')])
                if not path:
                        return
                
                for pair in self.tree.get_children():
                        self.tree.delete(pair)

                with open(path, 'r', newline='', encoding='utf=8') as file:
                        reader = csv.DictReader(file)
                        for line in reader:
                                datas = (line["Student No."], line[" Name"], line[" Email Address"], line[" Name of School"], line[" Region"])
                                self.tree.insert("", "end", values=datas)
                messagebox.showinfo("Succes", f'Data has been imported')


        
