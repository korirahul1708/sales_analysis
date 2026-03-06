import pandas as pd
import random
from datetime import datetime, timedelta

customers = ["Rahul","Aman","Priya","Sneha","Arjun"]
cities = ["Delhi","Mumbai","Bangalore","Hyderabad","Chennai"]

products = [
    ("Laptop","Electronics",60000),
    ("Phone","Electronics",25000),
    ("Tablet","Electronics",20000),
    ("Headphones","Electronics",3000),
    ("Keyboard","Accessories",1500)
]

rows = []

start_date = datetime(2024,1,1)

for i in range(1,5001):   # <-- THIS defines i
    product = random.choice(products)
    date = start_date + timedelta(days=random.randint(0,365))

    rows.append({
        "order_id": i,
        "date": date,
        "customer": random.choice(customers),
        "city": random.choice(cities),
        "product": product[0],
        "category": product[1],
        "quantity": random.randint(1,5),
        "price": product[2]
    })

df = pd.DataFrame(rows)

df.to_csv("sales_dataset_5000_rows.csv", index=False)

print("Dataset created successfully!")