def insert_into_table_invoice(conn, id,  nome, cnpj, endereco, marca):
  cursor = conn.cursor()
  sql = "INSERT INTO FORNECEDOR (ID_FORNECEDOR, NOME, CNPJ, ENDERECO, MARCA) values (%s, %s, %s, %s, %s)"
  value_table = (id, nome, cnpj, endereco, marca)
  cursor.execute(sql, value_table)
  cursor.close()
  conn.commit()

def select_element_in_table_invoice(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT ID_FORNECEDOR, NOME, CNPJ, ENDERECO, MARCA FROM FORNECEDOR")
  myresult = cursor.fetchall()

  return_string(myresult)
  
  cursor.close()
def return_string(element) -> str:
  for x in element:
    print(x)
  
def deleting_data_in_tables_invoice(conn, id):
  mycursor = conn.cursor()
  sql = "DELETE FROM FORNECEDOR WHERE NOME = %s"
  adr = (id,)
  mycursor.execute(sql, adr)
  conn.commit()
  print(mycursor.rowcount, "record(s) deleted") 

def update_in_tables_invoice(conn, nome_antigo, nome_aser_substituido):
  mycursor = conn.cursor()
  sql = "UPDATE FORNECEDOR SET NOME = %s WHERE NOME = %s"
  val = (nome_aser_substituido, nome_antigo)
  mycursor.execute(sql, val)
  conn.commit()
  print(mycursor.rowcount, "record(s) affected") 