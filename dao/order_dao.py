import psycopg2 as psycopg
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from model.models import Orders, OrderDetails
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def inserir_pedido_seguro(customer_id, employee_id, order_date, product_id, quantity):
    try:
        with psycopg.connect("dbname=northwind user=postgres password=Debouncing host=localhost") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT MAX(orderid) FROM northwind.orders")
                result = cur.fetchone()
                max_order_id = result[0] if result and result[0] is not None else 0
                order_id = max_order_id + 1

                cur.execute("""
                    INSERT INTO northwind.orders (orderid, customerid, employeeid, orderdate)
                    VALUES (%s, %s, %s, %s)
                """, (order_id, customer_id, employee_id, order_date))

                cur.execute("""
                    INSERT INTO northwind.order_details (orderid, productid, quantity)
                    VALUES (%s, %s, %s)
                """, (order_id, product_id, quantity))

                conn.commit()
                return True
    except Exception as e:
        print(f"[SEGURO] Erro ao inserir pedido: {e}")
        return False, e




def inserir_pedido_inseguro(customer_id, employee_id, order_date, product_id, quantity):
    try:
        with psycopg.connect("dbname=northwind user=postgres password=Debouncing host=localhost") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT MAX(orderid) FROM northwind.orders")
                result = cur.fetchone()
                max_order_id = result[0] if result and result[0] is not None else 0
                order_id = max_order_id + 1

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

    
def inserir_pedido_orm(customer_id, employee_id, order_date, product_id, quantity):
    engine = create_engine("postgresql+psycopg2://postgres:Debouncing@localhost/northwind")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        max_order_id = session.query(Orders).order_by(Orders.orderid.desc()).first()
        order_id = (max_order_id.orderid if max_order_id else 0) + 1
        new_order = Orders(orderid=order_id, customerid=customer_id, employeeid=employee_id, orderdate=order_date)
        session.add(new_order)
        new_order_detail = OrderDetails(orderid=order_id, productid=product_id, quantity=quantity)
        session.add(new_order_detail)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"[ORM] Erro ao inserir pedido: {e}")
        return False, e
    finally:
        session.close()