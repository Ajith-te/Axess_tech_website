# Python implementation to insert data into a table in MySQL
import mysql.connector
from faker import Faker
fake = Faker()
import random
# connecting to the mysql server

db = mysql.connector.connect(
host="localhost",
user="root",
passwd="",
database="test"
)

# cursor object c
c = db.cursor()


employeetbl_select = """SELECT * FROM skills"""

c.execute(employeetbl_select)

employee_data = c.fetchall()
for e in employee_data:
 print(e)

db.close()
'''
# insert statement for tblemployee
# this statement will enable us to insert multiple rows at once.
employeetbl_insert = """INSERT INTO skills (
Name,
skill,
level,
exp,
add1,
add2)
VALUES (%s, %s, %s, %s, %s, %s)"""

level_list = ['basic', 'advance', 'intermediate']
skill_list = ['sql', 'html', 'css','django','react','python','bootstrap','mongoDb']

data=[]
for i in range(1,500):
 data.append((fake.name(),random.choice(skill_list),random.choice(level_list) ,random.randint(1, 6),7,8))
# print(data)
# execute the insert commands for all rows and commit to the database
c.executemany(employeetbl_insert, data)
db.commit()

# finally closing the database connection
db.close()'''