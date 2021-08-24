from connection import close_connection

def insert_into_table(conn, id,  nome, cnpj, endereco, marca):
  cursor = conn.cursor()
  sql = "INSERT INTO FORNECEDOR (ID_FORNECEDOR, NOME, CNPJ, ENDERECO, MARCAS) values (%s, %s, %s, %s, %s)"
  value_table = (id, nome, cnpj, endereco, marca)
  cursor.execute(sql, value_table)
  cursor.close()
  conn.commit()

def select_element_in_table(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT NOME, CNPJ, ENDERECO, MARCAS FROM FORNECEDOR")
  myresult = cursor.fetchall()

  return_string(myresult)
  
  cursor.close()

def return_string(element) -> str:
  for x in element:
    print(x)
  