import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="dw_projeto",
    user="admin",
    password="1234"
)

print("Conectado!")