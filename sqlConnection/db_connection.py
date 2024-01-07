import pyodbc 

class DatabaseConnection:
  def __init__(self, server, database):
    self.__data_connection = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};"
    
 
  def start_connection(self):
    try:
      return pyodbc.connect(self.__data_connection)
    except:
      return False
    
  def get_cursor(self):
    return self.start_connection().cursor()
  