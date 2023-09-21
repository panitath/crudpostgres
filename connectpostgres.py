import pymysql
# สร้าง function เชื่อ


def connectdb():
    # connection = pymysql.connect(
    #     host='localhost',
    #     user='root',
    #     password='',
    #     db='pythondb',
    #     port=3306,
    #     cursorclass=pymysql.cursors.DictCursor

    connection = pymysql.connect(
        host='dpg-ck5snrr6fquc739cqou0-a',
        user='admin',
        password='u0r0E8RpBxTX9aWEcdcy3gvLDWwog3uQ',
        database='sampledb_9jcz',
        port=5432,
       
    )
    return connection
