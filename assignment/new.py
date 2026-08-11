import  mysql.connector

def connection():
 con = mysql.connector.connect(
    host="localhost",
    user="root",
    passward="root",
    database="registration"

  )
 return con



def add_student(name,roll):
      con=connection()
      cur=con.cursor ()

      query="""
      INSERT INTO students(name,roll)
      VALUES(%S,%S)
      """ 
      cur.execute(query,(name,roll))
       

      con.commit()
      con.close()