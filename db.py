import pyodbc
import urllib
import io
import pandas as pd
from sqlalchemy import create_engine, text

driver = 'ODBC Driver 17 for SQL Server'
server = '192.168.1.33,59958\\SQLEXPRESS01'
database = 'KPC_CHTM'
username = 'sa'
password = 'bejokun'

def get_connection():
    try:
        params = urllib.parse.quote_plus(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}')
        conn = create_engine(f'mssql+pyodbc:///?odbc_connect={params}')
        return conn
    except Exception as e:
        print(f"Gagal terhubung ke database: {e}")
        return 0

def show_all_tables():
    conn = get_connection()
    if not conn:
        return

    try:
        cursor = conn.connect()
        result = cursor.execute(text("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'"))
        tables = [row[0] for row in result.fetchall()]
        return tables
    except Exception as e:
        print(f"Gagal mengambil daftar tabel: {e}")

def data_csv(tables, date):
    conn = get_connection('download')
    if not conn:
        return
    else:
        query = f'SELECT * FROM [{database}].[dbo].[{tables}]'
        csv_buffer = io.StringIO()
        df = pd.read_sql(query, conn)
        df.to_csv(csv_buffer, index=False)
        csv_data = csv_buffer.getvalue()
        return csv_data

def data_excel(tables, date):
    conn = get_connection()
    if not conn:
        return
    else:
        query = f'SELECT * FROM [{database}].[dbo].[{tables}]'
        excel_buffer = io.BytesIO()
        df = pd.read_sql(query, conn)
        with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        excel_data = excel_buffer.getvalue()
        return excel_data
