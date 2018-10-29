# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 06:46:01 2018

@author: SKT
"""

import sqlite3
from sqlite3 import Error

def create_conn(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return None

def execute(conn, command):
    try:
        c = conn.cursor()
        c.execute(command)
    except Error as e:
        print(e)
        
def display_table(conn, table):    
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table)
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

if __name__ == "__main__":
    conn = create_conn('new.db')
    
    create_table = """ CREATE TABLE IF NOT EXISTS projects (
                            id integer PRIMARY KEY,
                            name text NOT NULL,
                            begin_date text,
                            end_date text
                    );"""
    
    execute(conn, create_table)
    
    insert1 = """INSERT INTO projects
                VALUES (1, 'skt', '01/01/2015', '02/02/2016')"""
                
    insert2 = """INSERT INTO projects
                VALUES (2, 'skt1', '02/02/2016', '03/03/2017')"""
    
                
    execute(conn, insert1)
    
    execute(conn, insert2)
    
    display_table(conn, "projects")
    
    conn.close()
    
    
    
 
