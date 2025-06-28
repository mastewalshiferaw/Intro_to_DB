import mysql.connector
from mysql.connector import Error

try:
    
    with mysql.connector.connect(
        host='localhost',
        user='Mastawal',
        password='20withGod25te'  
    ) as conn:
        
        
        with conn.cursor() as cursor:
            
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            
            
            print("Database 'alx_book_store' created successfully!")

except Error as e:
    
    print(f"Error: {e}")