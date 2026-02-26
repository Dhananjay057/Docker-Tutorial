from flask import Flask
import pymysql

app = Flask(__name__)

def db_connection():
    connection = pymysql.connect(
        host='mysql_container',
        user='root',
        password='demopassword',        
        database='demodb'
    )   
    return connection

@app.route('/')
def home():
    return "Hello Flask"

@app.route('/insert_data') 
def insert_data():
    connection = db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (city, temperature) VALUES ('New York', 25.5)")
    connection.commit()
    cursor.close()
    connection.close()
    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)