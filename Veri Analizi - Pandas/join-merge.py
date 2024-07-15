import pandas as pd

customers = {
    "CustomerId": [1, 2, 3, 4],
    "FirstName": ["Ahmet", "Ali", "Hasan", "Canan"],
    "LastName": ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

orders = {
    "OrderId": [10, 11, 12, 13],
    "CustomerId": [1, 2, 5, 7],
    "OrderDate": ["2010-07-04", "2010-08-04", "2010-07-07", "2012-07-04"]
}

df_customers = pd.DataFrame(customers, columns = ["CustomerId", "FirstName", "LastName"])
df_orders = pd.DataFrame(orders, columns = ["OrderId", "CustomerId", "OrderDate"])

print(df_customers)
print(df_orders)

# Inner Join, Left Join, Right Join, Outer Join => SQL'de de aynıları var.
result = pd.merge(df_customers, df_orders, how = "inner") # Her iki tabloda da olanları birleştiririz. Yani sipariş veren kişiler.
result = pd.merge(df_customers, df_orders, how = "left") # df_customers önceliklidir. Bütün müşteriler gelir. Sipariş vermeyenler (NaN) dahil.
result = pd.merge(df_customers, df_orders, how = "right") # df_orders önceliklidir.
result = pd.merge(df_customers, df_orders, how = "outer") # Her iki tablodaki tüm veriler birleştirilir.

customersA = {
    "CustomerId": [1, 2, 3, 4],
    "FirstName": ["Ahmet", "Ali", "Hasan", "Canan"],
    "LastName": ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

customersB = {
    "CustomerId": [4, 5, 6, 7],
    "FirstName": ["Yağmur", "Çınar", "Cengiz", "Can"],
    "LastName": ["Bilge", "Turan", "Yılmaz", "Turan"]
}

df_customersA = pd.DataFrame(customersA, columns = ["CustomerId", "FirstName", "LastName"])
df_customersB = pd.DataFrame(customersB, columns = ["CustomerId", "FirstName", "LastName"])

result = pd.concat([df_customersA, df_customersB]) # İki tablo alt alta birleştirilir.
result = pd.concat([df_customersA, df_customersB], axis = 1) # İki tablo yan yana birleştirilir.

print(result)
