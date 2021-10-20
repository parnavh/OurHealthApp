from dotenv import load_dotenv
from os import getenv
from mysql import connector
import datetime

class Mysql:
    def __init__(self):
        load_dotenv()
        connection = self.getConnection()
        cursor = connection.cursor(buffered=True)
        cursor.execute("create table if not exists login (username varchar(20) not null unique, password varchar(40))")
        cursor.execute("create table if not exists userdata (username varchar(20) not null unique, gender varchar(10), age int)")
        cursor.execute("create table if not exists appointments (username varchar(20), doctor varchar(20), date date, patient varchar(40))")
        cursor.execute("create table if not exists prescriptions (username varchar(20), filename varchar(20))")
        cursor.execute("create table if not exists reminders (username varchar(20), topic varchar(20), date date, description varchar(91))")
        cursor.close()
        connection.close()

    def getConnection(self):
        return connector.connect(
            host = getenv("SQL_URL"),
            user = getenv("SQL_USER"),
            passwd = getenv("SQL_PASSWORD"),
            database = getenv("SQL_DATABASE")
        )

    def execute(self, query):
        connection = self.getConnection()
        cursor = connection.cursor(buffered=True)
        try:
            cursor.execute(query)
            if cursor.rowcount > 0:
                connection.commit()
            else:
                cursor.rollback()
        except Exception as error: print(error)
        cursor.close()
        connection.close()

    def check_credentials(self, username, password):
        connection = self.getConnection()
        cursor = connection.cursor(buffered=True)
        name = None
        query = f"select username from login where username='{username}' and password='{password}'"
        try:
            cursor.execute(query)
            for (user) in cursor:
                name = user[0]
        except Exception as error: print(error)
        cursor.close()
        connection.close()
        return name

    def name_exists(self, name):
        val = False
        connection = self.getConnection()
        cursor = connection.cursor(buffered=True)
        query = (f"select username from login where username='{name}'")
        cursor.execute(query)
        for (name) in cursor:
            val = True
        cursor.close()
        connection.close()
        return val

    def get_reminders(self, name):
        val = []
        current_date = datetime.date.today().strftime('%y-%m-%d')
        connection = self.getConnection()
        cursor = connection.cursor(buffered=True)
        query = (f"select * from reminders where username='{name}' and date >= {current_date} order by date asc")
        cursor.execute(query)
        for (name, topic, date, description) in cursor:
            string = '{:60}\t\t\tDue:{}'.format(topic, str(date))
            val.append((string, description))
        cursor.close()
        connection.close()
        return val

    def get_age(self, name):
        val = None
        connection = self.getConnection()
        cursor = connection.cursor(buffered=True)
        query = (f"select age from userdata where username='{name}'")
        cursor.execute(query)
        for (age) in cursor:
            val = str(age[0])
        cursor.close()
        connection.close()
        return val