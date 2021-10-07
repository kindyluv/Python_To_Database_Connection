import mysql.connector as mysql
from mysql.connector import Error


# define the connector function
# password Loisdizz@123
def connect_fetch():
    """ function to connect and fetch rows in database"""

    # create a variable for the connector object
    conn = None

    # collecting user input local
    host = input("Enter host type: \n")
    database = input("Enter data base: \n")
    user = input("Enter user name: \n")
    password = input('Enter user password:\n')
    # print(password)

    # # connecting using our database parameters
    try:
        conn = mysql.connect(host=host, database=database,
                             user=user, password=password)
        print('Connecting to the database server')
        if conn.is_connected:
            print("connected to the database")

    #         # select query
    #         sql_select_query = "select * from human"
    #         cursor = conn.cursor()
    #         cursor.execute(sql_select_query)
    #         records = cursor.fetchall()
    #         print("Total number of rows in human is: ", cursor.rowcount)
    #
    #         # display data from database
    #         print("\nPrinting each Human record")
    #         records.insert(10, [11, "Ruth", "Black", "Female", "O+"])
    #         records.insert(11, [12, "Eric", "Yellow", "Male", "A+"])
    #         records.insert(12, [13, "Jada", "Yellow", "female", "B+"])
    #         records.insert(13, [14, "Jahson", "Yellow", "Male", "O-"])
    #         records.insert(14, [15, "Jahzeal", "Yellow", "female", "C-"])
    #         records.insert(15, [16, "Daniel", "Yellow", "Male", "D-"])
    #         records.insert(16, [17, "Delight", "Yellow", "female", "AB-"])
    #         for row in records:
    #             print("Human Id : ", row[0])
    #             print("Name : ", row[1])
    #             print("Color : ", row[2])
    #             print("Gender : ", row[3])
    #             print("Blood group : ", row[4], '\n')
    # except Error as e:
    #     print('Not connecting to: ', e)
    # finally:
    #     if conn is not None and conn.is_connected():
    #         conn.close()
    #         print("database shutdown")
    #

connect_fetch()
