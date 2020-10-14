import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="rishika",passwd="rishika105",database="rish")
mycursor = mydb.cursor()
mycursor.execute("use rish")
mycursor.execute("create table employees(email varchar(30),company_name varchar(20),company_id int(2),cricket_fan bit,football_fan bit)")
mycursor.execute("""insert into employees values("amit@gmail.com","abcd tech",34,1,1)""")
mydb.commit()
mycursor.execute("select * from employees")
print(mycursor.fetchall())