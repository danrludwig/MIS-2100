import psycopg2

try:
    connection = psycopg2.connect(user = 'postgres',
                                  password = 'oysome!1',
                                  host = 'localhost',
                                  port = '5432',
                                  database = 'boys_basketball'
    )

    cursor = connection.cursor()

    create_table_query = """ CREATE TABLE phone
        (ID INT PRIMARY KEY NOT NULL,
        MODEL TEXT NOT NULL,
        PRICE REAL);"""

    cursor.execute(create_table_query)
    connection.commit()
    print('Table created sucessfully in PostgreSQL')

    cursor.close()
    connection.close()

except (Exception, psycopg2.Error) as error:
    print('Error while connecting to PostgreSQL', error)




