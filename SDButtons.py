from SDData import SDData
import json
from tkinter import filedialog
import csv

class SDButtons:
    def __init__(self, init=False, SDName="SchoolDB.csv", SDJ="SchoolDB.json"):
        self.SDName = SDName
        self.SDJ = SDJ
        self.data=[]
        if init:
            print(f'Initializing {self.SDName}')

    def compiledata(self):
        tuples=[]
        for data in self.data:
            listdata = (data.studentno,
                        data.name,
                        data.email,
                        data.school,
                        data.region
                        )
            tuples.append(listdata)
        return tuples
        
    def addschool(self, studentno, name, email, school, region):
        newdata = SDData(studentno=studentno, name=name, email=email, school=school, region=region)
        self.data.append(newdata)
        print(f'Inserted student {name} into the database')

    def deleteschool(self, studentno):
        for x,y in enumerate(self.data):
            if y.studentno == studentno:
                del self.data[x]
                print(f'Student {studentno} is deleted in the database')
                return
            
    def updateschool(self, studentno, newname, newemail, newschool, newregion):
        for data in self.data:
            if data.studentno == studentno:
                data.name = newname
                data.email = newemail
                data.school = newschool
                data.region = newregion
                print(f'Student{studentno} is updated')
                return
        print(f'No Student {studentno} exists')

    def exportcsv(self):
        with open(self.SDName, 'w') as file:
            file.write("Student No., Name, Email Address, Name of School, Region\n")
            for data in self.data:
                file.write(f'{data.studentno}, {data.name}, {data.email}, {data.school}, {data.region}\n')
        print(f'Exported to {self.SDName}')

    def exportjson(self):
        jsondata=[]
        for data in self.data:
            jsondata.append({
                "Student No" : data.studentno,
                "Name" : data.name,
                "Email Address" : data.email,
                "Name of School" : data.school,
                "Region" : data.region
            })
        with open(self.SDJ, 'w') as file:
            json.dump(jsondata, file, indent=2)

        print(f'Exported to {self.SDJ}')
    
    def importcsv(self):
        path = filedialog.askopenfilename(filetypes=[('CSV Files','*.csv')])
        if not path:
            return

        
        self.data.clear()

        with open(path, 'r') as file:
            csvfile = csv.reader(file, delimiter=",")
            categories = []
            for line in csvfile:
                categories.append(line)
        if path:
            for otherline in categories[1:]:
                studentno, name, email, school, region = otherline
                self.addschool(studentno, name, email, school, region)
                print(f'Data has been imported.')

    def studentexists(self, studentno):
        for data in self.data:
            if data.studentno == studentno:
                return True
        return False
    
    