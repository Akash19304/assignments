import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Travel_Planner")
cursor.execute("USE Travel_Planner")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        user_id INT,
        flight_id INT,
        hotel_id INT,
        activity_id INT,
        booking_date DATE
    )
""")

cursor.execute("""
    INSERT INTO bookings (user_id, flight_id, hotel_id, activity_id, booking_date)
    VALUES
    (1, 101, 201, 301, '2024-08-01'),
    (2, 102, 202, 302, '2024-08-02'),
    (3, 103, 203, 303, '2024-08-03')
""")

connection.commit()

query = "SELECT * FROM bookings"
df = pd.read_sql(query, connection)

cursor.close()
connection.close()

print(df)
