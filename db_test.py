import psycopg2
DATABASE_URL = 'postgresql://username:password@localhost:5432/postgres'
conn = psycopg2.connect(dbname='postgres', user='username', password='password', host='localhost')
with conn.cursor() as curs:
    curs.execute('INSERT INTO test (id, name) VALUES (%s, %s)', (2, "John"))
    conn.commit()


