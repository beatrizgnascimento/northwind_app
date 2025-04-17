from dao.dao_base import DAOBase
import psycopg2 as psycopg

class DAOSeguro(DAOBase):
    def inserir_order(self,customer_name, employee_name, order_date):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT MAX(orderid) FROM northwind.orders")
                    result = cur.fetchone()
                    max_order_id = result[0] if result and result[0] is not None else 0
                    order_id = max_order_id + 1

                    cur.execute("SELECT customerid FROM northwind.customers WHERE contactname = %s", (customer_name,))
                    customer_result = cur.fetchone()
                    if not customer_result:
                        raise ValueError(f"Customer '{customer_name}' not found.")
                    customer_id = customer_result[0]
                    cur.execute("SELECT employeeid FROM northwind.employees WHERE firstname = %s", (employee_name,))
                    employee_result = cur.fetchone()
                    if not employee_result:
                        raise ValueError(f"Employee '{employee_name}' not found.")
                    employee_id = employee_result[0]

                    cur.execute("""
                        INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate)
                        VALUES (%s, %s, %s, %s)
                    """, (order_id, customer_id, employee_id, order_date))

                    conn.commit()
                    return (True, str(order_id))
        except Exception as e:
            print(f"[SEGURO] Erro ao inserir pedido: {e}")
            return (False, e)

    def inserir_order_detail(self, order_id, product_id, quantity, unit_price, discount):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(f"""
                        INSERT INTO northwind.order_details (orderid, productid, quantity, unitprice, discount)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (order_id,product_id, quantity, unit_price, discount))
                    conn.commit()
                    return (True, "")
        except Exception as e:
            print(f"[SEGURO] Erro ao inserir detalhes do pedido: {e}")
            return (False, e)

    def relatorio_order(self, order_id):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    ret = ""
                    cur.execute("""
                        SELECT o.orderid, o.orderdate, c.contactname, e.firstname
                        FROM northwind.orders o
                        JOIN northwind.customers c ON o.customerid = c.customerid
                        JOIN northwind.employees e ON o.employeeid = e.employeeid
                        WHERE o.orderid = %s
                    """, (order_id,))
                    result = cur.fetchall()
                    ret = "ID do Pedido: " + str(result[0][0]) + "\n"
                    ret += "Data do Pedido: " + str(result[0][1]) + "\n"
                    ret += "Nome do Cliente: " + str(result[0][2]) + "\n"
                    ret += "Nome do Vendedor: " + str(result[0][3]) + "\n"
                    ret += "\n\nProdutos:\n"
                    cur.execute("""
                        SELECT p.productname, od.quantity, od.unitprice, od.discount
                        FROM northwind.order_details od
                        JOIN northwind.products p ON od.productid = p.productid
                        WHERE od.orderid = %s
                    """, (order_id,))
                    result = cur.fetchall()
                    for row in result:
                        ret += f"Produto: {row[0]}, Quantidade: {row[1]}, Preço Unitário: {row[2]}, Desconto: {row[3]}\n"
                    return ret
        except Exception as e:
            print(f"[SEGURO] Erro ao gerar relatório do pedido: {e}")
            return None

    def relatorio_employee(self, date_start, date_end):
        try:
            with self.get_connection() as conn:
                with conn.cursor() as cur:
                    ret = ""
                    cur.execute("""
                        SELECT e.firstname, SUM(od.quantity * od.unitprice * (1 - od.discount)) AS total_sales
                        FROM northwind.employees e
                        JOIN northwind.orders o ON e.employeeid = o.employeeid
                        JOIN northwind.order_details od ON o.orderid = od.orderid
                        WHERE o.orderdate BETWEEN %s AND %s
                        GROUP BY e.firstname
                        ORDER BY total_sales DESC
                    """, (date_start, date_end))
                    result = cur.fetchall()
                    i = 1
                    for row in result:
                        ret += f"#{i} Vendedor: {row[0]}, Total de Vendas: {row[1]}\n"
                        i += 1
                    return ret
        except Exception as e:
            print(f"[SEGURO] Erro ao gerar relatório de vendas por vendedor: {e}")
            return None
        