Por favor execute o seguinte código no banco de dados!!
```sql
ALTER TABLE northwind.order_details
ADD CONSTRAINT fk_order_details_orders
FOREIGN KEY (orderid)
REFERENCES northwind.orders (orderid);

ALTER TABLE northwind.order_details
ADD CONSTRAINT fk_order_details_products
FOREIGN KEY (productid)
REFERENCES northwind.products (productid);

ALTER TABLE northwind.orders
ADD CONSTRAINT fk_orders_customers
FOREIGN KEY (customerid)
REFERENCES northwind.customers (customerid);

ALTER TABLE northwind.orders
ADD CONSTRAINT fk_orders_employees
FOREIGN KEY (employeeid)
REFERENCES northwind.employees (employeeid);
```