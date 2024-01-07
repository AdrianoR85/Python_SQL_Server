from db_connection import DatabaseConnection
from sales_data import SaleData
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SERVER')
database = os.getenv('DATABASE')

def main():
  connection_manager = DatabaseConnection(server, database)
  
  if not connection_manager.start_connection():
    print('Connection Failed')
    return
  

  client = input('Client Name: ')
  product = input('Product Name: ')
  quantity = int(input('Quantity: '))
  price = float(input('Price: '))
  date = input('Date: ')
  
  
  try:
    cursor = connection_manager.get_cursor()
  
    sale = SaleData(cursor, client, product, quantity, price, date)
    query = SaleData.sale_query(sale)

    sale.execute_query(query)
    print('Sale completed successfully') 
  except:
    print('Sale Not Completed')
  
main()
