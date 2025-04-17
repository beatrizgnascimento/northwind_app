from dao.dao_base import DAOBase
import psycopg2 as psycopg

class DAOInseguro(DAOBase):
    def inserir_order(self,customer_name, employee_name, order_date, product_id, quantity):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT MAX(orderid) FROM northwind.orders")
                    result = cur.fetchone()
                    max_order_id = result[0] if result and result[0] is not None else 0
                    order_id = max_order_id + 1


                    cur.execute(f"SELECT customerid FROM northwind.customers WHERE customername = {customer_name}")
                    customer_result = cur.fetchone()
                    if not customer_result:
                        raise ValueError(f"Customer '{customer_name}' not found.")
                    customer_id = customer_result[0]
                    cur.execute(f"SELECT employeeid FROM northwind.employees WHERE employeename = {employee_name}")
                    employee_result = cur.fetchone()
                    if not employee_result:
                        raise ValueError(f"Employee '{employee_name}' not found.")
                    employee_id = employee_result[0]

                    query_order = f"""
                        INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate)
                        VALUES ({order_id}, '{customer_id}', {employee_id}, '{order_date}')
                    """
                    print("[INSEGURO] Executando:\n", query_order)
                    cur.execute(query_order)

                    query_details = f"""
                        INSERT INTO northwind.order_details (orderid, productid, quantity)
                        VALUES ({order_id}, {product_id}, {quantity})
                    """
                    cur.execute(query_details)

                    conn.commit()
                    return True
        except Exception as e:
            print(f"[INSEGURO] Erro ao inserir pedido: {e}")
            return False, e

    def inserir_order_detail(self, customer_id, employee_id, order_date, product_id, quantity):
        pass

    def relatorio_order(self, order_id):
        pass

    def relatorio_employee(self, date_start, date_end):
        pass