import sqlite3
from flask import request

def dict_factory(cursor, row):
    map = {}
    for idx, col in enumerate(cursor.description):
        # [(0, ('price',None,None,None,...)), (1, ('symbol',None,None,,))]
        map[col[0]] = row[idx]
    return map

def get_conn():
    conn = sqlite3.connect('example.db')
    conn.row_factory = dict_factory
    return conn

def insert_txn():
    conn = get_conn()
    try:
        c = conn.cursor()

        txn = (
            request.form.get("date"),
            request.form.get("trans"),
            request.form.get("symbol"),
            request.form.get("qty"),
            request.form.get("price"),
        )

        c.execute('INSERT INTO stocks (date, trans, symbol, qty, price) VALUES (?,?,?,?,?)',
            txn)        
        conn.commit()

        return "{'status':'ok'}"
    except:
        return ("{'status':'error'",500)
    finally:
        conn.close()


def get_all_txn():
    conn = get_conn()
    try:
        c = conn.cursor()

        rows = c.execute('SELECT * FROM stocks')
            
        return str(rows.fetchall())
    finally:
        conn.close()

def get_txn_by_code(code):
    conn = get_conn()
    try:
        c = conn.cursor()

        rows = c.execute('SELECT * FROM stocks WHERE symbol = ?', 
            (code,)).fetchall()
            
        return str(rows)
    finally:
        conn.close()
