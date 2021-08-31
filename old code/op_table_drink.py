
def insert_into_table_drink(conn, id,  nome, recipiente, teor_alcolico, sabor, gaseficado, retornavel, bebida_tipo):
  cursor = conn.cursor()
  sql = "INSERT INTO PEDIDO (ID_PEDIDO, ITENS PRECO) values (%s, %s, %s)"
  value_table = (id,  nome, recipiente, teor_alcolico, sabor, gaseficado, retornavel, bebida_tipo)
  cursor.execute(sql, value_table)
  cursor.close()
  conn.commit()

def select_element_in_table_drink(conn):
  cursor = conn.cursor()
  cursor.execute("SELECT ID_BEBIDA, NOME, RECIPIENTE, TEOR_ALCOLICO, SABOR, GASEFICADO, RETORNAVEL, BEBIDA_TIPO FROM BEBIDA")
  myresult = cursor.fetchall()

  return_string(myresult)
  
  cursor.close()
  
def return_string(element) -> str:
  for x in element:
    print(x)
  
def deleting_data_in_tables_drink(conn, id):
  mycursor = conn.cursor()
  sql = "DELETE FROM BEBIDA WHERE NOME = %s"
  adr = (id,)
  mycursor.execute(sql, adr)
  conn.commit()
  print(mycursor.rowcount, "record(s) deleted") 

def update_in_tables_drink(conn, nome_antigo, nome_aser_substituido):
  mycursor = conn.cursor()
  sql = "UPDATE BEBIDA SET NOME = %s WHERE NOME = %s"
  val = (nome_aser_substituido, nome_antigo)
  mycursor.execute(sql, val)
  conn.commit()
  print(mycursor.rowcount, "record(s) affected") 