import pandas as pd
import sqlite3

# 讀取Excel文件
excel_file = '交易.xlsx'  # 將 'your_file.xlsx' 替換為您的Excel文件路徑
df = pd.read_excel(excel_file)

# 創建或連接到SQLite數據庫
db_file = 'output.db'  # 將 'output.db' 替換為您想要的數據庫文件名稱
conn = sqlite3.connect(db_file)

# 將DataFrame寫入SQLite數據庫
df.to_sql('stock_data', conn, if_exists='replace', index=False)

# 關閉數據庫連接
conn.close()

print(f'Excel文件已成功轉換為SQLite數據庫：{db_file}')
