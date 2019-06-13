import sqlite3
conn = sqlite3.connect('example.db')

# Create table
try:
    conn.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
except:
    pass

purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
conn.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

conn.commit()

conn.close()