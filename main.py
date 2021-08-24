#!/usr/bin/python
from connection import connection, close_connection
from operantion_table import select_element_in_table

def main():
    conn = connection( "172.17.0.2", "root", "root", "buteco")

    insert_into_table(conn, "2", "", "24516783", "meuquiadis bonifasio espindula", "")

    select_element_in_table(conn)

    close_connection(conn)


if __name__ == "__main__":
    main()
