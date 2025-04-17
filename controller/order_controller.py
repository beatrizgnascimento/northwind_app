class Controller:
    def __init__(self, dao):
        self.dao = dao

    def criar_pedido(self, dados):
        return self.dao.inserir_order(
            customer_name=dados["customer_name"],
            employee_name=dados["employee_name"],
            order_date=dados["order_date"],
        )
    def gerar_relatorio_order(self, dados):
        return self.dao.gerar_relatorio_order(
            order_id=dados["order_id"]
        )
    def gerar_relatorio_employee(self, dados):
        return self.dao.gerar_relatorio_employee(
            date_start=dados["date_start"],
            date_end=dados["date_end"]
        )