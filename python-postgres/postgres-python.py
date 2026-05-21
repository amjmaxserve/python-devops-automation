import psycopg2
from psycopg2 import sql

# Connect to PostgreSQL database
conn = psycopg2.connect(
    host="192.168.29.7",
    port=5432,
    database="postgres",   # connect to default DB
    user="myuser",
    password="mypassword"
)

# Enable autocommit
conn.autocommit = True

# Create a cursor object
cur = conn.cursor()

# Connection check
cur.execute("SELECT version()")
version = cur.fetchone()

print("PostgreSQL version:", version[0])

if conn:
    print("Connection to PostgreSQL database successful!")
else:
    print("Connection to PostgreSQL database failed.")

# List of databases to create
databases = ["mydatabase1", "mydatabase2", "mydatabase3"]

# Create databases safely
for db in databases:

    # Check if database already exists
    cur.execute(
        "SELECT 1 FROM pg_database WHERE datname = %s",
        (db,)
    )

    exists = cur.fetchone()

    if not exists:
        cur.execute(sql.SQL("CREATE DATABASE {}").format(
            sql.Identifier(db)
        ))
        print(f"Database '{db}' created successfully")

    else:
        print(f"Database '{db}' already exists")

# View all databases
cur.execute("SELECT datname FROM pg_database")

all_databases = cur.fetchall()

print("\nDatabases:")

for db in all_databases:
    print(db[0])

# Close cursor and connection
cur.close()
conn.close()