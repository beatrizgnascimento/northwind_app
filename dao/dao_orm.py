from dao.dao_base import DAOBase
import psycopg2 as psycopg
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from model.models import Orders, OrderDetails
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DAOOrm(DAOBase):
    def inserir_order(self, customer_id, employee_id, order_date, product_id, quantity):
        engine = self.get_engine
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

    def inserir_order_detail(self, customer_id, employee_id, order_date, product_id, quantity):
        pass

    def relatorio_order(self, order_id):
        pass

    def relatorio_employee(self, date_start, date_end):
        pass