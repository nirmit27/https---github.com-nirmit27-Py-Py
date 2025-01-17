import mysql.connector as msc
from mysql.connector import Error as mscError


def connect(creds=[]):
    host = ''
    db = ''
    user = ''
    pwd = ''
    connection = any

    if len(creds) == 4:
        host = creds[0]
        db = creds[1]
        user = creds[2]
        pwd = creds[3]

    if len(creds) < 4:
        host = input("Enter host name : ")
        db = input("Enter database name : ")
        user = input("Enter username : ")
        pwd = input("Enter password : ")

    try:
        connection = msc.connect(
            user=user,
            password=pwd,
            host=host,
            database=db
        )
        print(f"\nConnected successfully!")
        return connection

    except mscError as e:
        print(f"\nConnection error - {e}\n")
        return None


def query(c):
    if c is not None:
        cursor = c.cursor(dictionary=True)

        q = input("\nEnter your query :\n\n")
        cursor.execute(q)

        print(f"\n\nQuery ran successfully! Results :\n\n")
        result = cursor.fetchall()

        for row in result:
            print(row, end='\n\n')
    return


if __name__ == "__main__":
    connection = connect(['localhost', 'nirmit27', 'Pwd12345_'])
    query(connection)
