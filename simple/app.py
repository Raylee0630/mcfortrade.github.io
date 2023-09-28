from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def display_table():
    # 連接到SQLite數據庫
    conn = sqlite3.connect('output.db')  # 請確保數據庫文件名稱與之前創建的數據庫文件名稱一致
    cursor = conn.cursor()
    
    # 檢索數據庫中的表格數據
    cursor.execute('SELECT * FROM stock_data')
    data = cursor.fetchall()
    
    # 關閉數據庫連接
    conn.close()
    
    # 呈現HTML模板，並將數據傳遞給模板
    return render_template('table.html', data=data)

if __name__ == '__main__':
    app.run()
