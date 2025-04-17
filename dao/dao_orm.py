from dao.dao_base import DAOBase
import psycopg2 as psycopg
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from model.models import Orders, OrderDetails
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DAOOrm(DAOBase):
    def inserir_order(self, customer_name, employee_name, order_date):
        engine = self.get_engine
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            max_order_id = session.query(Orders).order_by(Orders.orderid.desc()).first()
            customer = session.query(Orders).filter(Orders.contactname == customer_name).first()
            if not customer:
                raise ValueError(f"Customer '{customer_name}' not found.")
            customer_id = customer.customerid
            employee = session.query(Orders).filter(Orders.firstname == employee_name).first()
            if not employee:
                raise ValueError(f"Employee '{employee_name}' not found.")
            employee_id = employee.employeeid
            order_id = (max_order_id.orderid if max_order_id else 0) + 1
            new_order = Orders(orderid=order_id, customerid=customer_id, employeeid=employee_id, orderdate=order_date)
            session.add(new_order)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"[ORM] Erro ao inserir pedido: {e}")
            return False, e
        finally:
            session.close()

    def inserir_order_detail(self, order_id, product_id, quantity, unit_price, discount):
        pass

    def relatorio_order(self, order_id):
        pass

    def relatorio_employee(self, date_start, date_end):
        pass