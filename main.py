#!/usr/bin/python
from connection import connection, close_connection
from operantion_table import *

def main():
    conn = connection( "172.17.0.2", "root", "root", "buteco")
    if interface_selct == 1:
        print('insira nome, cnpj, localição, marcas')
        insert_into_table(conn, "2", "", "24516783", "meuquiadis bonifasio espindula", "")
    elif interface_selct == 1.1:
        select_element_in_table(conn)
    
    deleting_data_in_tables(conn)

    update_in_tables(conn)

    close_connection(conn)


if __name__ == "__main__":
    main()
