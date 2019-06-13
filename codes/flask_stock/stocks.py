import sqlite3
from flask import jsonify, request

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    db = sqlite3.connect('example.db')
    db.row_factory = dict_factory
    return db

def get_all_txn():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM stocks")
    try:
        return jsonify(c.fetchall())
    finally:
        conn.close()

def insert_txn():
    try:
        conn = get_db()
        c = conn.cursor()
        date = request.form.get('date')
        price = float(request.form.get('price'))
        qty = int(request.form.get('qty'))
        symbol = request.form.get('symbol')
        trans = request.form.get('trans')

        c.execute("INSERT INTO stocks values (?,?,?,?,?)", (date, price, qty, symbol, trans)) #pass as tuple
        conn.commit()
        return ("{'status':'ok'}", 200)
    except:
        return (jsonify({'status':'error'}), 500)
    finally:
        conn.close()

def get_txn_by_code(code):
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT * FROM stocks where symbol = ?", (code,)) #pass as tuple
    try:
        return jsonify(c.fetchall())
    finally:
        conn.close()

