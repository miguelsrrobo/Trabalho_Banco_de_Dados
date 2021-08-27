#!/usr/bin/python
from connection import *
from op_table_provider import *
from op_table_drink import *
from op_table_request import *
from interface import *

def main():
    conn = connection( "172.17.0.2", "root", "root", "buteco")
    interface_bank()
    interface_selct_position = input(':')
    
    if interface_selct_position == '1':
        supplier_interface()
        interface_selct_position = input(':')
        if interface_selct_position == '1':
            print('insira id, nome, cnpj, localição, marcas')
            id = int(input(':'))
            nome = input(':')
            cnpj = int(input(':'))
            endereco = input(':')
            marca = input(':')
            insert_into_table(conn, id, nome, cnpj, endereco, marca)
        elif interface_selct_position == '2':
            select_element_in_table(conn)
        elif interface_selct_position == '3':
            nome = ''
            id = int(input(':'))
            deleting_data_in_tables(conn, nome)
        elif interface_selct_position == '4':
            nome_antigo = input(':')
            nome_aser_substituido = input(':')
            update_in_tables(conn, nome_antigo, nome_aser_substituido)
        else:
            exit(1)
    else:
        exit(1)   
    
    close_connection(conn)


if __name__ == "__main__":
    main()
