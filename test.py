

import psycopg2
print(psycopg2.__version__)

connect=psycopg2.connect(dbname="postgres",
user="postgres",
password="123",
host="localhost",
port="5433")

print("Connected successfully")
