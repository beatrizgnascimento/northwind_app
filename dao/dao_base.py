class DAOBase:
    def __init__(self, get_connection, get_engine):
        self.get_connection = get_connection
        self.get_engine = get_engine
    def inserir_order(self,customer_name, employee_name, order_date, product_id, quantity):
        pass
    def inserir_order_detail(self,customer_id, employee_id, order_date, product_id, quantity):
        pass
    def relatorio_order(self,order_id):
        pass
    def relatorio_employee(self,date_start, date_end):
        pass