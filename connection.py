import mysql.connector 

def connection(host_machine, user_bank, password_bank, bank_bank):
  return mysql.connector.connect(host = host_machine, user = user_bank, password = password_bank, database = bank_bank)

def close_connection(conn):
  return conn.cursor()
