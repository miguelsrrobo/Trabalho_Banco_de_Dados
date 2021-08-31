def insert_into_table_manufacturer(conn, id, marca):
  cursor = conn.cursor()
  sql = "INSERT INTO FORNECEDOR (ID_FABRICANTE, MARCA) values (%s, %s, %s, %s, %s)"
  value_table = (id, marca)
  cursor.execute(sql, value_table)
  cursor.close()
  conn.commit()

def select_element_in_table_manufacturer(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT ID_FABRICANTE MARCA FROM FABRICANTE")
  myresult = cursor.fetchall()

  return_string(myresult)
  
  cursor.close()
def return_string(element) -> str:
  for x in element:
    print(x)
  
def deleting_data_in_tables_manufacturer(conn, id):
  mycursor = conn.cursor()
  sql = "DELETE FROM FABRICANTE WHERE MARCA = %s"
  adr = (id,)
  mycursor.execute(sql, adr)
  conn.commit()
  print(mycursor.rowcount, "record(s) deleted") 

def update_in_tables_manufacturer(conn, nome_antigo, nome_aser_substituido):
  mycursor = conn.cursor()
  sql = "UPDATE FABRICANTE SET MARCA = %s WHERE MARCA = %s"
  val = (nome_aser_substituido, nome_antigo)
  mycursor.execute(sql, val)
  conn.commit()
  print(mycursor.rowcount, "record(s) affected") 