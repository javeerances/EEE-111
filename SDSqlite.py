import sqlite3

class SDSqlite:
    def __init__(self, SDName='SchoolDB.db'):
        super().__init__()
        self.SDName = SDName
        self.csvFile = self.SDName.replace('.db', '.csv')
        self.connect = sqlite3.connect(self.SDName)
        self.cursor = self.connect.cursor()
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Students(
                        studentno TEXT PRIMARY KEY,
                        name TEXT,
                        email TEXT,    
                        school TEXT,    
                        region TEXT)''')
        self.connect.commit()
        self.connect.close()

    def connect_cursor(self):
        self.connect = sqlite3.connect(self.SDName)
        self.cursor = self.connect.cursor()

    def commit_close(self):
        self.connect.commit()
        self.connect.close()

    def create_table(self):
        self.connect_cursor()
        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Students(
                        studentno TEXT PRIMARY KEY,
                        name TEXT,
                        email TEXT,    
                        school TEXT,    
                        region TEXT)''')
        self.commit_close()

    def compiledata(self):
        self.connect_cursor()
        self.cursor.execute('SELECT * FROM Students')
        students = self.cursor.fetchall()
        self.connect.close()
        return students
        
    def addschool(self, studentno, name, email, school, region):
        self.connect_cursor()
        self.cursor.execute('INSERT INTO Students (student no, name, email, school, region) VALUES (?, ?, ?, ?, ?)',
                            (studentno, name, email, school, region))
        self.commit_close()

    def deleteschool(self, studentno):
        self.connect_cursor()
        self.cursor.execute('DELETE FROM Students WHERE studentno = ?', (studentno))
        self.commit_close()
            
    def updateschool(self, studentno, newname, newemail, newschool, newregion):
        self.connect_cursor()
        self.cursor.execute('UPDATE Students WHERE studentno = ? SET name = ?, email = ?, school = ?, region = ?',
                        (studentno, newname, newemail, newschool, newregion))
    
    def exortcsv(self):
        with open(self.csvFile, 'w') as filehandle:
            SDName = self.compiledata()
            for data in SDName:
                print(data)
                filehandle.write(f'{data[0]},{data[1]},{data[2]},{data[3]},{data[4]}\n')

    def studentexists(self, studentno):
        self.connect_cursor()
        self.cursor.execute('SELECT COUNT(*) FROM Students WHERE studentno = ?', (studentno))
        result = self.cursor.fetchone()
        self.connect.close()
        return result[0] > 0
    