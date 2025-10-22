from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "I'm not sure, but it's okey"})

@app.route('/db')
def db_test():
    try:
        conn = psycopg2.connct(os.environ['DATABASE_URL'])
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
