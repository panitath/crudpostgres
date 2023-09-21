import psycopg2

def connectdb():

    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1234',
        database='sampledb',
        port=5432,
        
    )
    return connection

# print(connectdb())

