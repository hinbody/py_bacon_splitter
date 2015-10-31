import mysql.connector as mydb

#create a database, grant the appropriate privileges, then change the
#information below to match

db_config = {
    'user': 'bacon',
    'password': 'bacon',
    'database': 'bacon'
}

conn = mydb.connect(**db_config)
my_cursor = conn.cursor()
my_cursor.execute('''CREATE TABLE IF NOT EXISTS creditors(
                id int NOT NULL AUTO_INCREMENT, name varchar(30) NOT NULL, phone char(12),
                address varchar(50), email varchar(50), account_number
                varchar(20), type varchar(15), PRIMARY KEY(id))''')

conn.commit()
conn.close()
