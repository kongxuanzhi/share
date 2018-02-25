from flask import Flask, jsonify, abort
import tushare as ts
# print(ts.get_hist_data('600848',start='2015-01-05',end='2015-01-09'))
app = Flask(__name__)
print(ts.get_today_all())

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)