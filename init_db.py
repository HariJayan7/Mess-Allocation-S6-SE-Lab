import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Mess_Details (Mess_Id,Mess_Name,Allocated,Capacity) VALUES (?,?,?,?)",
            (1, "Mess A", 0, 10)
            )
cur.execute("INSERT INTO Mess_Details (Mess_Id,Mess_Name,Allocated,Capacity) VALUES (?,?,?,?)",
            (2, "Mess B", 0, 10)
            )
cur.execute("INSERT INTO Mess_Details (Mess_Id,Mess_Name,Allocated,Capacity) VALUES (?,?,?,?)",
            (3, "Mess C", 0, 10)
            )
cur.execute("INSERT INTO Mess_Details (Mess_Id,Mess_Name,Allocated,Capacity) VALUES (?,?,?,?)",
            (4, "Mess D", 0, 10)
            )
cur.execute("INSERT INTO Mess_Details (Mess_Id,Mess_Name,Allocated,Capacity) VALUES (?,?,?,?)",
            (5, "Mess E", 0, 10)
            )

cur.execute("SELECT * from Mess_Details")
items = cur.fetchall()
for item in items:
    print(item)

cur.execute("INSERT INTO Hostel_Warden VALUES (?,?,?)",
            ("warden_1", "Abhay Raj", 1)
            )
cur.execute("INSERT INTO Hostel_Warden VALUES (?,?,?)",
            ("warden_2", "Aaron Joseph", 2)
            )
cur.execute("INSERT INTO Hostel_Warden VALUES (?,?,?)",
            ("warden_3", "Harinarayanan", 3)
            )
cur.execute("INSERT INTO Hostel_Warden VALUES (?,?,?)",
            ("warden_4", "Manideep Reddy", 4)
            )
cur.execute("INSERT INTO Hostel_Warden VALUES (?,?,?)",
            ("warden_5", "Vishnu Babu", 5)
            )
cur.execute("SELECT * from Hostel_Warden")
items = cur.fetchall()
for item in items:
    print(item)
cur.execute("INSERT INTO Hostel_Details VALUES (?,?)",
            (1, 'Hostel A')
            )
cur.execute("INSERT INTO Hostel_Details VALUES (?,?)",
            (2, 'Hostel B')
            )
cur.execute("INSERT INTO Hostel_Details VALUES (?,?)",
            (3, 'Hostel C')
            )
cur.execute("INSERT INTO Hostel_Details VALUES (?,?)",
            (4, 'Hostel D')
            )
cur.execute("INSERT INTO Hostel_Details VALUES (?,?)",
            (5, 'Hostel E')
            )
cur.execute("SELECT * from Hostel_Details")
items = cur.fetchall()
for item in items:
    print(item)

cur.execute("INSERT INTO Mess_Manager VALUES (?,?,?)",
            ("Manager_1", "Abhiram", 1)
            )
cur.execute("INSERT INTO Mess_Manager VALUES (?,?,?)",
            ("Manager_2", "John", 2)
            )
cur.execute("INSERT INTO Mess_Manager VALUES (?,?,?)",
            ("Manager_3", "Gautham", 3)
            )
cur.execute("INSERT INTO Mess_Manager VALUES (?,?,?)",
            ("Manager_4", "Khalid", 4)
            )
cur.execute("INSERT INTO Mess_Manager VALUES (?,?,?)",
            ("Manager_5", "Noah", 5)
            )
cur.execute("SELECT * from Mess_Manager")
items = cur.fetchall()
for item in items:
    print(item)
connection.commit()
connection.close()
