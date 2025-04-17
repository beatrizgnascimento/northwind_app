from dao.dao_base import DAOBase
import psycopg2 as psycopg
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from model.models import Customers, Employees, Orders, OrderDetails, Employees
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func

class DAOOrm(DAOBase):
    def inserir_order(self, customer_name, employee_name, order_date):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            max_order_id = session.query(Orders).order_by(Orders.orderid.desc()).first()
            customer = session.query(Customers).filter(Customers.contactname == customer_name).first()
            if not customer:
                raise ValueError(f"Customer '{customer_name}' not found.")
            customer_id = customer.customerid
            employee = session.query(Employees).filter(Employees.firstname == employee_name).first()
            if not employee:
                raise ValueError(f"Employee '{employee_name}' not found.")
            employee_id = employee.employeeid
            order_id = (max_order_id.orderid if max_order_id else 0) + 1
            new_order = Orders(orderid=order_id, customerid=customer_id, employeeid=employee_id, orderdate=order_date)
            session.add(new_order)
            session.commit()
            return (True, "")
        except Exception as e:
            session.rollback()
            print(f"[ORM] Erro ao inserir pedido: {e}")
            return (False, e)
        finally:
            session.close()

    def inserir_order_detail(self, order_id, product_id, quantity, unit_price, discount):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()
        try:
            new_order_detail = OrderDetails(orderid=order_id, productid=product_id, quantity=quantity, unitprice=unit_price, discount=discount)
            session.add(new_order_detail)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            print(f"[ORM] Erro ao inserir detalhe do pedido: {e}")
            return False, e
        finally:
            session.close()

    def relatorio_order(self, order_id):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            order = session.query(Orders).filter(Orders.orderid == order_id).first()
            if not order:
                raise ValueError(f"Pedido com ID '{order_id}' não encontrado.")
            customer = session.query(Orders).filter(Orders.customerid == order.customerid).first()
            employee = session.query(Orders).filter(Orders.employeeid == order.employeeid).first()
            order_details = session.query(OrderDetails).filter(OrderDetails.orderid == order_id).all()
            ret = f"ID do Pedido: {order.orderid}\n"
            ret += f"Data do Pedido: {order.orderdate}\n"
            ret += f"Nome do Cliente: {customer.contactname}\n"
            ret += f"Nome do Vendedor: {employee.firstname}\n"
            ret += "\n\nProdutos:\n"
            for detail in order_details:
                product = session.query(Orders).filter(Orders.productid == detail.productid).first()
                ret += f"Produto: {product.productname}, Quantidade: {detail.quantity}, Preço Unitário: {detail.unitprice}, Desconto: {detail.discount}\n"

        except Exception as e:
            print(f"[ORM] Erro ao gerar relatório do pedido: {e}")
            return False, e
        finally:
            session.close()

    def relatorio_employee(self, date_start, date_end):
        engine = self.get_engine()
        Session = sessionmaker(bind=engine)
        session = Session()

        try:
            employees = session.query(Employees.firstname,func.sum(OrderDetails.quantity * OrderDetails.unitprice * (1 - OrderDetails.discount)))\
            .join(Employees.orders).join(Orders.order_details).filter(Orders.orderdate.between(date_start,date_end)).\
            group_by(Employees.firstname).order_by(func.sum(OrderDetails.quantity * OrderDetails.unitprice * (1 - OrderDetails.discount)).desc()).all()
            #employees = session.query(Employees.firstname,).order_by(Employees.total_sales.desc()).all()
            ret = "Relatório de Vendas por Funcionário:\n"
            print(employees)
            i = 1
            for employee in employees:
                ret += f"#{i} Vendedor: {employee[0]}, Total de Vendas: {employee[1]}\n"
                i += 1
            return ret
        except Exception as e:
            print(f"[ORM] Erro ao gerar relatório de funcionários: {e}")
            return False, e
        finally:
            session.close()