class SaleData:
  def __init__(self, cursor, client, product, quantity, price, date):
    self.cursor = cursor
    self.client = client
    self.product = product
    self.quantity = quantity
    self.price = price
    self.date = date
  
  def sale_query(self):
    return f"""
      INSERT INTO sales(
      client_name, 
      product_name,
      product_quantity,
      product_price,
      sale_date 
    ) VALUES (
     '{self.client}', '{self.product}', {self.quantity}, {self.price}, '{self.date}'
    )
    """
  
  def execute_query(self, query):
    self.cursor.execute(query)
    self.cursor.commit()
    self.cursor.close()
    