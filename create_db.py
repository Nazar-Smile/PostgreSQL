import psycopg2

conn = psycopg2.connect(database="nazar_db", user="nazar", password="pulsar", host="127.0.0.1", port=5432)

cur = conn.cursor()

create_db_query = "CREATE DATABASE nazar_db;"
cur.execute(create_db_query)

create_user_query = "CREATE USER nazar WITH PASSWORD 'pulsar'"
cur.execute(create_user_query)

grant_privileges_query = "GRANT ALL PRIVILEGES ON DATABASE nazar_db TO nazar"
cur.execute(grant_privileges_query)

cur.close()

conn.commit()

conn.close()

