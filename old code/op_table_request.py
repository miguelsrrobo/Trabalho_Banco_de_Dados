
def insert_into_table_request(conn, id,  iten, preco):
  cursor = conn.cursor()
  sql = "INSERT INTO PEDIDO (ID_PEDIDO, ITEN PRECO) values (%s, %s, %s)"
  value_table = (id,  iten, preco)
  cursor.execute(sql, value_table)
  cursor.close()
  conn.commit()

def select_element_in_table_request(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT ID_PEDIDO ITEN PRECO FROM PEDIDO")
  myresult = cursor.fetchall()

  return_string(myresult)
  
  cursor.close()
def return_string(element) -> str:
  for x in element:
    print(x)
  
def deleting_data_in_tables_request(conn, id):
  mycursor = conn.cursor()
  sql = "DELETE FROM PEDIDO WHERE ITEN = %s"
  adr = (id,)
  mycursor.execute(sql, adr)
  conn.commit()
  print(mycursor.rowcount, "record(s) deleted") 

def update_in_tables_request(conn, nome_antigo, nome_aser_substituido):
  mycursor = conn.cursor()
  sql = "UPDATE PEDIDO SET ITEN = %s WHERE ITEN = %s"
  val = (nome_aser_substituido, nome_antigo)
  mycursor.execute(sql, val)
  conn.commit()
  print(mycursor.rowcount, "record(s) affected") 