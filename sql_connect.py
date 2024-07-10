'''code to connect mysql with python to setup operations. 
we'll have to figure out the frontend connection separately.'''

import mysql.connector

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="localhost",
    user="bharathi",
    password="idlydosa",
    database="your_database" #replace this
)

# Create a cursor object to execute SQL queries
cursor = db_connection.cursor()

# Execute a simple SQL query
cursor.execute("SELECT * FROM your_table")

# Fetch and print the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and database connection
cursor.close()
db_connection.close()




