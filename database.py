import sqlite3


def query(query_text, *param):
    conn = sqlite3.connect ('Northwind_large.sqlite')
    cur = conn.cursor()
    cur.execute(query_text, param)

    column_names = []
    for column in cur.description:
        column_names.append(column[0])

    print(column_names)
    rows = cur.fetchall()

    dicts= []
    for row in rows:
        d = dict(zip(column_names, row))
        dicts.append(d)
    conn.close()
    return dicts


def get_all_suppliers():
    return query("""SELECT COUNT (Product.Id) AS ProductCount, Supplier.CompanyName, Supplier.City, Supplier.Country, Supplier.Id
FROM Product

INNER JOIN SUpplier
	ON Product.SupplierId = Supplier.Id
	
GROUP BY CompanyName""")

def get_supplier_products(supplier_id):
    return query("""SELECT * FROM Product WHERE SupplierId = ? """, supplier_id )

def get_categories():
    return query("""SELECT Category.CategoryName, Category.Description, Category.Id, COUNT (Product.CategoryId) AS ProductCount FROM Product

INNER JOIN Category
	ON Product.CategoryId = Category.Id

GROUP BY CategoryId """)

def get_category_products(category_id):
    return query("""SELECT * FROM Product INNER JOIN Supplier ON Product.SupplierId = Supplier.Id WHERE CategoryId = ? """, category_id )