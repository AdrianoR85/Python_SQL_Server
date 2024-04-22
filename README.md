# Sales Data Management System

This is a simple Python script designed for  establishing a connection to a SQL Server database and performing sales data insertion.
This script was developed for practice and learning."

## Setup

1. Install the required dependencies:

   ```bash
   pip install pyodbc python-dotenv
  
2. Create a .env file in the project directory and add your database connection details:
    ```ini
    SERVER=your_server_name
    DATABASE=your_database_name
   ```
4. Run the Script
   ```bash
   python main.py

## Usage
1. Input the required information:
- Client Name
- Product Name
- Quantity
- Price
- Date
  
2. The script will attempt to establish a connection to the specified SQL Server database.
- If the connection is successful, it will prompt you to input details for a sale.
- If the connection fails, it will display a "Connection Failed" message.

3. After entering the sale details, the script will attempt to insert the data into the 'sales' table.
- If successful, it will display a "Sale completed successfully" message.
- If unsuccessful, it will display a "Sale Not Completed" message.

## Code Structure
### Database Connection (db_connection.py)
This module defines a DatabaseConnection class, which manages the connection to the SQL Server database.

### Sale Data (sales_data.py)
This module defines a SaleData class, representing sales data and containing methods for constructing SQL queries and executing them.

### Main Script (main.py)
The main script utilizes the DatabaseConnection and SaleData classes to handle user input, establish a database connection, and perform sales data insertion.

## Dependencies
- pyodbc: Python ODBC bridge.
- python-dotenv: Reads the key-value pair from .env file and adds them to the environment variable.

  
Feel free to contribute, report issues, or suggest improvements!
