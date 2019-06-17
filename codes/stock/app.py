from flask import Flask
import handler 

app = Flask(__name__)

app.add_url_rule('/txn/', view_func = handler.insert_txn,
    methods = ['POST'])

app.add_url_rule('/txn/', view_func = handler.get_all_txn,
    methods = ['GET'])

app.add_url_rule('/txn/<code>', view_func = handler.get_txn_by_code,
    methods = ['GET'])

if __name__ == '__main__':
    app.run(debug=True)

