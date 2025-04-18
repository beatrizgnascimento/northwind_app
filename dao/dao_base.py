class DAOBase:
    def __init__(self, get_connection, get_engine):
        self.get_connection = get_connection
        self.get_engine = get_engine
    def inserir_order(self,customer_name, employee_name, order_date):
        pass
    def inserir_order_detail(self, order_id, product_id, quantity, unit_price, discount):
        pass
    def relatorio_order(self, order_id):
        pass
    def relatorio_employee(self,date_start, date_end):
        pass