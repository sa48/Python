from flask import Flask
import stocks

app=Flask(__name__)
app.add_url_rule('/txn',view_func=stocks.get_all_txn, methods=['GET'])
app.add_url_rule('/txn/<code>',view_func=stocks.get_txn_by_code, methods=['GET'])
app.add_url_rule('/txn',view_func=stocks.insert_txn, methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)


