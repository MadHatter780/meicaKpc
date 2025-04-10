import streamlit as st
import pandas as pd
import io

driver = 'ODBC Driver 17 for SQL Server'
server = '192.168.1.33,59958\\SQLEXPRESS01'
database = 'KPC_CHTM'
username = 'sa'
password = 'bejokun'

def get_connection():
    try:
        conn = st.connection(
            "sql",
            dialect="mssql",
            driver="pyodbc",
            host=server,
            database=database,
            username=username,
            password=password,
            query={
                "driver": driver,
                "encrypt": "no" 
            }
        )
        return conn
    except Exception as e:
        print(f"Gagal terhubung ke database: {e}")
        return 0

def show_all_tables():
    conn = get_connection()
    if not conn:
        return

    try:
        result = conn.query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'")
        tables = result['TABLE_NAME'].to_list()
        return tables
    except Exception as e:
        print(f"Gagal mengambil daftar tabel: {e}")
    
def data_csv(tables, date):
    conn = get_connection()
    if not conn:
        return
    else:
        query_dump = f'SELECT * FROM [{database}].[dbo].[{tables}] WHERE 1=0'
        dump = conn.query(query_dump)
        data_dump = dump.columns.to_list()
        if 'DATE' in data_dump:
            query = f'SELECT * FROM [{database}].[dbo].[{tables}] WHERE [DATE] = {date}'
            csv_buffer = io.StringIO()
            df = conn.query(query)
            df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()
        else:
            query = f'SELECT * FROM [{database}].[dbo].[{tables}] WHERE [DateTime] = {date}'
            csv_buffer = io.StringIO()
            df = conn.query(query)
            df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()
        return csv_data

def data_excel(tables, date):
    conn = get_connection()
    if not conn:
        return
    else:
        query_dump = f'SELECT * FROM [{database}].[dbo].[{tables}] WHERE 1=0'
        dump = conn.query(query_dump)
        data_dump = dump.columns.to_list()
        if 'DATE' in data_dump:
            query = f'SELECT * FROM [{database}].[dbo].[{tables}] WHERE [DATE] = {date}'
            excel_buffer = io.BytesIO()
            df = conn.query(query)
            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            excel_data = excel_buffer.getvalue()
        else:
            query = f'SELECT * FROM [{database}].[dbo].[{tables}] WHERE [DateTime] = {date}'
            excel_buffer = io.BytesIO()
            df = conn.query(query)
            with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            excel_data = excel_buffer.getvalue()
        return excel_data
